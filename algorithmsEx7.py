# make a function that will sort a list from least to greates value 
def listSorter(jointLists, min, sortedList):
    # every new minimum number that we are finding we remove from the joint list until we have an empty list
    while len(jointLists)>0:
        #we are looping through our list and comparing it to the minimum value in search for a smaller number
        for number in jointLists:
            if min>number:
                # if a smaller number is found then that is set as the new minimum
                min = number
        # now that we have our smallest value, remove it from jointList and add it to the sortedList. 
        # This way, we can loop through jointLists and find a new minimum value
        sortedList.append(min)
        jointLists.remove(min)
        # make sure min exists and if it doesn't then continue without stopping the program
        try:
            min = jointLists[0]
        except:
            pass
    print(sortedList)


numList1 = [3,6,9,3,5,1,0]
numList2 = [4,-1,-5,7,2,8,-9] 
# we are joining both lists to go over in a single loop
jointLists = numList1 + numList2
sortedList = []
min = jointLists[0]

# call the function that sorts a list to sort jointLists
listSorter(jointLists, min, sortedList)

































# numList1 = [3,6,9,3,5,1,0]
# numList2 = [4,-1,-5,7,2,8,-9] 
# # we are joining both lists to go over in a single loop
# jointLists = numList1 + numList2
# sortedList = []
# min = jointLists[0]
# # every new minimum number that we are finding we remove from the joint list until we have an empty list
# while len(jointLists)>0:
#     #we are looping through our list and comparing it to the minimum value in search for a smaller number
#     for number in jointLists:
#         if min>number:
#             # if a smaller number is found then that is set as the new minimum
#             min = number
#     # now that we have our smallest value, remove it from jointList and add it to the sortedList. 
#     # This way, we can loop through jointLists and find a new minimum value
#     sortedList.append(min)
#     jointLists.remove(min)
#     # make sure min exists and if it doesn't then continue without stopping the program
#     try:
#         min = jointLists[0]
#     except:
#         pass


# print(sortedList)

# #IT WORKS!!!!!
