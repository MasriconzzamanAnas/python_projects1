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
        
    



