class Person:
    def _init_(self, name, age, cid):
        self.name = name
        self.age = age
        self.cid = cid

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Teacher(Person):
    def _init_(self, name, age, cid, subject, salary, department, designation):
        super()._init_(name, age, cid)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

class Student(Person):
    def _init_(self, name, age, cid, student_id, course, year, gpa):
        super()._init_(name, age, cid)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying {self.course}.")

    def attend_class(self):
        print(f"{self.name} is attending a class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")

# Create objects
teacher = Teacher("John Doe", 40, "123456", "Math", 50000, "Mathematics", "Professor")
student = Student("Jane Doe", 20, "654321", "1001", "Computer Science", 2, 3.5)

# Call methods
teacher.walk()
student.study()