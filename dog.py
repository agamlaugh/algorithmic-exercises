class Dog:
    def __init__(self, name, legs,  eyes, tail, fur):
        self.name = name
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.fur = fur
    def bark(self):
        print("I am ", self.name)

iDog = Dog("Grohl", 3, 2, 1, "white and black")
aDog = Dog("Liv", 4, 2, 1, "white and tan")

# print("I am ", iDog.name, "and my fur is ", iDog.fur)
# print("I am ", aDog.name, "and my fur is ", aDog.fur)

iDog.bark()
aDog.bark()



# legs = 4
#     eyes = 2
#     tail = 1
#     fur = "white with tan spots"
#     def bark():
#         print("I am a dog!")

# dog1 = Dog()
# print(dog1.legs)
# dog1.bark()