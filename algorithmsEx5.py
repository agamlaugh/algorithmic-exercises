numList = [3, 6, 7, 9, 1, 2, 0, 3, 5, 9, -1, 8]
counter = 0
# create a variable that stores the minimum value of the list
min = numList[counter]
# run loop until all of numList has been checked
while counter < len(numList):
    # check if the current minimum value is less than the value next to it. if not, the adjacent value becomes the new minimum
    if min > numList[counter]:
        min = numList[counter]
    counter = counter + 1
# find index of minimum value
index = numList.index(min)
print(min, " - ", index)
#hi
#works