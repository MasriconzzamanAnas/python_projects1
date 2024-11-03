import json

# Person Class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

# Student Class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def display_student_info(self):
        self.display_person_info()
        print(f"Student ID: {self.student_id}")
        print(f"Enrolled Courses: {', '.join(self.courses) if self.courses else 'None'}")
        print(f"Grades: {self.grades if self.grades else 'None'}")

# Course Class
class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor}")
        print("Enrolled Students:", ', '.join([student.name for student in self.students]) if self.students else 'None')

# Student Management System Class
class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, name, age, address, student_id):
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            student = Student(name, age, address, student_id)
            self.students[student_id] = student
            print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self, course_name, course_code, instructor):
        if course_code in self.courses:
            print("Course code already exists.")
        else:
            course = Course(course_name, course_code, instructor)
            self.courses[course_code] = course
            print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self, student_id, course_code):
        # check if student and course exists in the system before enrolling them in the course.
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        if student and course:
            student.enroll_course(course.course_name)
            course.add_student(student)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Student ID or Course Code does not exist.")

    def add_grade_for_student(self, student_id, course_code, grade):
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        if student and course and course.course_name in student.courses:
            student.add_grade(course.course_name, grade)
            print(f"Grade {grade} added for {student.name} in {course.course_name}.")
        else:
            print("Enrollment not found or invalid student/course ID.")

    def display_student_details(self, student_id):
        student = self.students.get(student_id)
        if student:
            student.display_student_info()
        else:
            print("Student ID does not exist.")

    def display_course_details(self, course_code):
        course = self.courses.get(course_code)
        if course:
            course.display_course_info()
        else:
            print("Course Code does not exist.")

    def save_data(self, filename="data.json"):
        data = {
            "students": {sid: {"name": s.name, "age": s.age, "address": s.address, "student_id": s.student_id,
                               "grades": s.grades, "courses": s.courses} for sid, s in self.students.items()},
            "courses": {cc: {"course_name": c.course_name, "course_code": c.course_code, "instructor": c.instructor,
                             "students": [s.student_id for s in c.students]} for cc, c in self.courses.items()}
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("All student and course data saved successfully.")

    def load_data(self, filename="data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.students = {sid: Student(name=s["name"], age=s["age"], address=s["address"], student_id=s["student_id"])
                             for sid, s in data["students"].items()}
            self.courses = {cc: Course(course_name=c["course_name"], course_code=c["course_code"], instructor=c["instructor"])
                            for cc, c in data["courses"].items()}
            for sid, s in data["students"].items():
                student = self.students[sid]
                student.grades = s["grades"]
                student.courses = s["courses"]
            for cc, c in data["courses"].items():
                course = self.courses[cc]
                for sid in c["students"]:
                    if sid in self.students:
                        course.add_student(self.students[sid])
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("Data file not found.")

# CLI Menu
def main():
    system = StudentManagementSystem()
    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")

        option = input("Select Option: ")
        if option == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            system.add_student(name, age, address, student_id)
        elif option == "2":
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            system.add_course(course_name, course_code, instructor)
        elif option == "3":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            system.enroll_student_in_course(student_id, course_code)
        elif option == "4":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            system.add_grade_for_student(student_id, course_code, grade)
        elif option == "5":
            student_id = input("Enter Student ID: ")
            system.display_student_details(student_id)
        elif option == "6":
            course_code = input("Enter Course Code: ")
            system.display_course_details(course_code)
        elif option == "7":
            system.save_data()
        elif option == "8":
            system.load_data()
        elif option == "0":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()



