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

class Whale:
    def __init__(self, type, size, weight):
        self.type = type
        self.size = size
        self.weight = weight
    def whaleNoise(self):
        print("OoooooOOO")
    def description(self):
        print(f"Whales are a {self.size} animal. These {self.type} weigh between {self.weight}.")

z = Whale("mammal", "large", "600lbs to 200tons")
z.whaleNoise()
z.description()

class BlueWhale(Whale):
    def __init__(self, type, size, weight, amountleft, dangerlevel):
        super().__init__(type, size, weight)
        self.amountleft = amountleft
        self.dangerlevel = dangerlevel
    def description(self):
        print(f"Blue Whales are a(n) {self.size} {self.type} that weigh between {self.weight}. There are only {self.amountleft} left and they are {self.dangerlevel} dangerous.")

w = BlueWhale("mammal", "enormous", "290,000 to 330,000 pounds", 25000, "not")
w.description()








# ideas
# phone(size, color, shape, weight, brand)
# ihpone(model, feature,)

# computer(size, color, s)
# phone