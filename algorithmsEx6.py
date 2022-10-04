from re import S


print('Enter how many values you want in your list:') 
inputAmount = int(input())
numList = [] 
print(f"Enter {inputAmount} values:")
#create a for loop to input values as much as the user previously instructed
for numValue in range(inputAmount):
    numList.append(input())
newList = []
# store a variable to know when there a duplicate number is found
duplicateFound = False 

#begin by adding the first value of numList to the empty list. without a value in the newlist the future for loops will not run. 
newList.append(numList[0])

# create a loop to go through each value in numList
for numValue in numList:
    # create a loop to go through each value in newList
    for newValue in newList:
        # put a conditional to check if the values from both lists are equal. if so, there is a duplicate number and the computer must be informed.
        if numValue == newValue:
            duplicateFound = True
    # Once the loop runs through all of newList, if there wasn't a duplicate then the value in numList is added to the newList.
    if duplicateFound == False:
        newList.append(numValue)
    # reset our variable that stores duplicates so that the updated lists can be checked again
    duplicateFound = False
print(newList)













# while len(numList) > 0:
#     while duplicateFound == False and counter < len(newList): #please replace while with for loop and insert coinfound condition inside loop in an if statement
#         if numList[0] == newList[counter]:
#             duplicateFound = True
#         else:
#             counter = counter + 1
#     counter = 0
#     if duplicateFound == False:
#         newList.append(numList[0])
#         numList.pop(0)
#     else:
#         numList.pop(0)
#         duplicateFound = False
# print(newList)

