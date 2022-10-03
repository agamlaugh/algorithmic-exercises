class Character:
    def __init__(self, name, eyes, hair, age, height, weight):
        self.name = name
        self.eyes = eyes
        self.hair = hair
        self.age = age
        self.height = height
        self.weight = weight
    def greet(self):
        print(f"Hello, my name is {self.name}")
    def getEyes(self):
        return self.eyes
    def getHair(self):
        return self.hair

class Eyes:
    def __init__(self, color, amount, shape):
        self.color = color
        self.amount = amount
        self.shape = shape
    def getColor(self):
        return self.color

class Hair:
    def __init__(self, color, type, texture, length):
        self.color = color
        self.type = type
        self.texture = texture
        self.length = length
    def getColor(self):
        return self.color

agam = Character("Agam", Eyes("brown", 2, "almond"), Hair("brown", "straight", "smooth", "long"), 17, 5.3, 115)

print(agam.getEyes().getColor())

print(agam.eyes.getColor())