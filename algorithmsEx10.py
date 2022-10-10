# create a class that holds four values
class twoCoordinates:
    def __init__(self, x1, y1, x2, y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
    # create functions to return the values
    def getValue1(self):
        return self.x1
    def getValue2(self):
        return self.y1
    def getValue3(self):
        return self.x2
    def getValue4(self):
        return self.y2


# create a function to find the slope of two points
def slopeFinder(x1, y1, x2, y2):
    yDel = float(y1 - y2)
    xDel = float(x1 - x2)
    slope = float(yDel/xDel)
    # return slope value
    return slope


# create a function to find the y-intercept
def findyInter(x1, y1, slope):
    yInter = float(y1 - (slope * x1))
    return yInter


# create a class to print the equation
class Equation:
    def __init__(self, slope, yInter):
        self.slope = slope
        self.yInter = yInter
    def equationPrinter(self):
        # show user the equation built from both points
        print(f"y = {slope}x + {yInter}")


# create a function that asks the user to choose x or y
def chooseVariable():
    chosenVariable = ""
    # create a loop that will end once the user doesn't input y or x for chosenVariable. 
    # The goal is to force the user to choose either x or y.
    while chosenVariable != "y" and chosenVariable != "x":
        chosenVariable = input("Enter y or x to get its corresponding value in a coordinate: ")
        if chosenVariable != "y" and chosenVariable != "x":
            print("You must type y or x: ")
    return chosenVariable


# create a function that prints a coordinate based on a value inputed for x or y
def printCoordinate():
    # once x or y is selected, let the user input a value. 
    # Then calculate the coordiante and print it
    if chosenVariable == "y":
        print("Enter y value: ")
        y = float(input())
        x = float((y - yInter)/slope)
        print(f"({x}, {y})")
        return {"x": x, "y":y}
    if chosenVariable == "x":
        print("Enter x value: ")
        x = float(input())
        y = float(slope*x + yInter)
        print(f"({x}, {y})")
        return {"x": x, "y":y}


# use the coordinates class. have user input coordiante values. make the input values floats
coordinates = twoCoordinates(float(input("Enter the x value of the first coordiante: " )), float(input("Enter the y value of the first coordiante: " )), float(input("Enter the x value of the second coordiante: " )), float(input("Enter the y value of the second coordiante: " )))        

x1 = coordinates.getValue1()
y1 = coordinates.getValue2()
x2 = coordinates.getValue3()
y2 = coordinates.getValue4()

# call the slope function to find the slope based on the coordinates given
slope = slopeFinder(x1, y1, x2, y2)

# call the intercept function to calculate the y-intercept
yInter = findyInter(x1, y1, slope)

# use the equation class to store the equation made by the two points
equation = Equation(slope, yInter)
# call the function in the equation class in order to print the equation
equation.equationPrinter()

# call the function that has the user choose x or y and store it in chosenVariable
chosenVariable = chooseVariable()

#call the function that prints the coordinate based on the inputed value
printCoordinate()


# send input and output history to new file
f = open("/Users/meytallitmanovitz/coding/algorithmic-exercises/algorithmsEx10outputs.txt", "a")
f.write(f"{equation} --> {printCoordinate}\n")
f.close()












































# # have user input coordiante values. make the input values floats 
# print("Enter the x value of the first coordiante:")
# x1 = float(input())
# print("Enter the y value of the first coordiante:")
# y1 = float(input())
# print("Enter the x value of the second coordiante:")
# x2 = float(input())
# print("Enter the y value of the second coordiante:")
# y2 = float(input())

# # find the slope
# yDel = float(y1 - y2)
# xDel = float(x1 - x2)
# slope = float(yDel/xDel)

# # find the y-intercept
# yInter = float(y1 - (slope * x1))

# # show user the equation built from both points
# print("y = ", slope, "x", " + ", yInter)


# chosenVariable = ""
# # create a loop that will end once the user doesn't input y or x for chosenVariable. 
# # The goal is to force the user to choose either x or y.
# while chosenVariable != "y" and chosenVariable != "x":
#     chosenVariable = input("Enter y or x to get its corresponding value in a coordinate: ")
#     if chosenVariable != "y" and chosenVariable != "x":
#         print("You must type y or x: ")

# # once x or y is selected, let the user input a value. 
# # Then calculate the coordiante and print it
# if chosenVariable == "y":
#     print("Enter y value: ")
#     y = float(input())
#     x = float((y - yInter)/slope)
#     print(f"({x}, {y})")
# if chosenVariable == "x":
#     print("Enter x value: ")
#     x = float(input())
#     y = float(slope*x + yInter)
#     print(f"({x}, {y})")

#works!!!

# Very good! 
# Please see exercise 11 from the document and continue it here!
# GOOD LUCK! you'll need it ;)