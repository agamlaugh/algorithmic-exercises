from re import A

x1 = y1 = x2 = y2 = 1

print("Enter the x value of the first coordiante:")
x1 = int(input())
print("Enter the y value of the first coordiante:")
y1 = int(input())
print("Enter the x value of the second coordiante:")
x2 = int(input())
print("Enter the y value of the second coordiante:")
y2 = int(input())

yDif = y1 - y2
xDif = x1 - x2
slope = yDif/xDif

yInter = y1 - slope * x1

print("y = ", slope, "x", " + ", yInter)

#works!!!

# Very good! 
# Please see exercise 11 from the document and continue it here!
# GOOD LUCK! you'll need it ;)