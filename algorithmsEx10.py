# have user input coordiante values. make the input values floats 
print("Enter the x value of the first coordiante:")
x1 = float(input())
print("Enter the y value of the first coordiante:")
y1 = float(input())
print("Enter the x value of the second coordiante:")
x2 = float(input())
print("Enter the y value of the second coordiante:")
y2 = float(input())

# find the slope
yDel = float(y1 - y2)
xDel = float(x1 - x2)
slope = float(yDel/xDel)

# find the y-intercept
yInter = float(y1 - (slope * x1))

# show user the equation built from both points
print("y = ", slope, "x", " + ", yInter)


chosenVariable = ""
# create a loop that will end once the user doesn't input y or x for chosenVariable. 
# The goal is to force the user to choose either x or y.
while chosenVariable != "y" and chosenVariable != "x":
    chosenVariable = input("Enter y or x to get its corresponding value in a coordinate: ")
    if chosenVariable != "y" and chosenVariable != "x":
        print("You must type y or x: ")

# once x or y is selected, let the user input a value. 
# Then calculate the coordiante and print it
if chosenVariable == "y":
    print("Enter y value: ")
    y = float(input())
    x = float((y - yInter)/slope)
    print(f"({x}, {y})")
if chosenVariable == "x":
    print("Enter x value: ")
    x = float(input())
    y = float(slope*x + yInter)
    print(f"({x}, {y})")



#works!!!

# Very good! 
# Please see exercise 11 from the document and continue it here!
# GOOD LUCK! you'll need it ;)