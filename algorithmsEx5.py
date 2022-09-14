numList = [3, 6, 7, 9, 1, 2, 0, 3, 5, 9, -1, 8]
counter = 0
min = numList[counter]
while counter < len(numList):
    if min > numList[counter]:
        min = numList[counter]
    counter = counter + 1
index = numList.index(min)
print(min, " - ", index)

#works