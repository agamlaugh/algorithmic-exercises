
# keep inputing numbers until a string is put
numList = [] 
print("Enter list values: ")
# create a loop that will end/break once the input is not an integer
while len(numList) >= 0:
    try: 
        numList.append(int(input()))
    except:
        break

newList = []
# store a variable to know when there is a duplicate number is found
duplicateFound = False 

# begin by adding the first value of numList to the empty list. 
# without a value in the newlist the for loops will not run. 
newList.append(numList[0])

for numValue in numList:
    for newValue in newList:
        # if the value from newList and numList are equal than we update our duplicateFound variable
        if numValue == newValue:
            duplicateFound = True
    # once the loop runs through the entire newList, 
    # if no duplicate then the value in numList is added to the newList.
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


# print('Enter how many values you want in your list:') 
# inputAmount = int(input())
# numList = [] 
# print(f"Enter {inputAmount} values:")
# #create a for loop to input values as much as the user previously instructed
# for numValue in range(inputAmount):
#     numList.append(input())
