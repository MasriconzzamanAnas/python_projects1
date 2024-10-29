import json

# Person Class design And Implementation
class Persons:

    def __init__(self, name, age, address):
        self.name = name
        self.age= age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

# Student Class design And Implementation
class Student(Persons):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address) #? calling the parent class constructor
        self.student_id = student_id
        self.grades ={}
        self.coruse = []


    def add_grades(self, subject, great):
        self.grades[subject] = great

    def enroll_course(self, course):
        if course not in self.coruse:
            self.coruse.append(course)
    
    def show_student_info(self):
        self.show_student_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: ({','.join(self.coruse) if self.coruse else 'None'}")
        print(f"Grades: {self.grades if self.grades else "None"}")


# Course 
class Course:
    
    def __init__(self, courseName, courseCode, instructor):
        self.courseNeme= courseName
        self.courseCode = courseCode
        self.instructor = instructor
        self.student_enroll= []

    def add_student(self,student):
        if student not in self.student_enroll:
            self.student_enroll.append(student)
        else:
            print("Student is already enrolled in this course")
        
    def course_info(self):
        print(f"Course information: Name: {self.courseNeme}, Code: {self.courseCode}, InstructorName: {self.instructor}")
        print('Enroll Student:',",".join([self.student_enroll]) if self.student_enroll else "none")

    
#Section B (system menagement)
class Student_management_System:
    def __init__(self):
        self.students= {}
        self.course = {}

    def add_student(self, name, age, address, student_id):
        if student_id is self.students:
            print('The student alrady exists')
        else:
            student= self.students(name,age,address, student_id)
            self.students[student_id] = student
            print(f"Student {name} (student_id: {student_id}) add successfuly")

    def add_course(self, courseName, courseCode, instructor):
        if courseCode in self.course:
            print('The course already exists')
        else:
            course = self.course(courseName, courseCode, instructor)
            self.course[courseCode] = course
            print(f"Course {courseName} (course_id: {courseCode})  create with the Instructor {instructor}")

    def enroll_student_in_course(self, courser_coud, studentId):
        # check if student and course exists in the system before enrolling them in the course.
        students= self.students.get(studentId)
        course = self.course.get(courser_coud)

        if students and course:
            students.enroll_course(course.courseName)
            course.add_student(students)
            print(f"Student {studentId} enrolled successfully in Course {course.courseName} course code: {courser_coud}")
        else:
            print('Either student or course does not exist')

    def add_great_for_student(self, student_id, courseCode, great):
        # check if student and course exists in the system before enrolling them in the course
        student = self.students.get(student_id)
        course = self.course.get(courseCode)

        if student_id and course:
            student.add_grades(course.courseName, great)
            print(f"Great added to student {student_id} for the {course.courseName}")
        else:
            print('Either student or course does not exist')

    def display_student_Details(self, student_id):
        student = self.students.get(student_id)
        if student:
            student.show_student_info()
        else:
            print(f'Student with id {student_id} does not exist')



