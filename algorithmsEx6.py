# print('Enter 7 values for a list:')
# numList = [input(), input(), input(), input(), input(), input(), input()]
# newList = []
# counter = 1 

# for counter in  range(1, 6):
#     if numList[counter] == newList[counter-1]:
#         print(numList[counter], "is a duplicate number")
#     else:
#         newList.append(numList[counter])
        
# print(newList)

# #doesn't work

from re import S


print('Enter 7 values for a list:')
numList = [input(), input(), input(), input(), input(), input(), input()]
newList = []
coinfound = False
counter = 0

newList.append(numList[0])
numList.pop(0)

while len(numList) > 0:
    while coinfound == False and counter < len(newList):
        if numList[0] == newList[counter]:
            coinfound = True
        else:
            counter = counter + 1
    counter = 0
    if coinfound == False:
        newList.append(numList[0])
        numList.pop(0)
    else:
        numList.pop(0)
        coinfound = False
print(newList)

#I SOLVED IT!!!!!! This took so many tries but I finally figured out my issue in the code! I had to reset counter to 0 so that every number in newList was being checked to numList.
    