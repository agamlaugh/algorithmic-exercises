class Person:
    def __init__(self, fname, lname, age, height, eyes, hair):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.height = height
        self.eyes = eyes
        self.hair = hair
    def greet(self):
        print(f"Hi, I'm {self.fname}!")

class Teacher(Person):
    def __init__(self, fname, lname, age, height, eyes, hair, subject, school, grade):
        super().__init__(fname, lname, age, height, eyes, hair)
        self.subject = subject
        self.school = school
        self.grade = grade
    def greet(self):
        print(f"Hello {self.grade} grade, I'm Mr/s {self.lname}, and I will be your {self.subject} teacher this year. I hope you all enjoy your year with me at {self.school}!")

x = Teacher("Mary", "Anne", 35, 5.4, "brown", "blonde", "Math", "Agoura High School", "12th")
x.greet()

class Student(Person):
    def __init__(self, fname, lname, age, height, eyes, hair, school, grade, gpa):
        super().__init__(fname, lname, age, height, eyes, hair)
        self.school = school
        self.grade = grade
        self.gpa = gpa
    def greet(self):
        print(f"Hey! I'm {self.fname}, {self.lname}. I'm in {self.grade} grade and I go to {self.school}. I have a gpa of {self.gpa}.")

y = Student("Agam", "Cohen", 17, 5.3, "brown", "brown", "Agoura High School", "12th", "4.0")
y.greet()