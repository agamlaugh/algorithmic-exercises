# create a function that find the minimum value and its index in a list
def minFinder(counter, list, min):
    # run loop until all of a list has been checked
    while counter < len(list):
        # check if the current minimum value is less than the value next to it. 
        # if not, the adjacent value becomes the new minimum
        if min > list[counter]:
            min = list[counter]
        counter = counter + 1
    # find index of minimum value
    index = list.index(min)
    print(min, " - ", index)

numList = [3, 6, 7, 9, 1, 2, 0, 3, 5, 9, -1, 8]
counter = 0
min = numList[counter]

# call the minFinder to find the smallest number in numList
minFinder(counter, numList, min)

# send input and output history to new file
f = open("/Users/meytallitmanovitz/coding/algorithmic-exercises/algorithmsEx5outputs.txt", "a")
f.write(f"{numList} --> {min}\n")
f.close()





















# numList = [3, 6, 7, 9, 1, 2, 0, 3, 5, 9, -1, 8]
# counter = 0
# # create a variable that stores the minimum value of the list
# min = numList[counter]
# # run loop until all of numList has been checked
# while counter < len(numList):
#     # check if the current minimum value is less than the value next to it. 
#     # if not, the adjacent value becomes the new minimum
#     if min > numList[counter]:
#         min = numList[counter]
#     counter = counter + 1
# # find index of minimum value
# index = numList.index(min)
# print(min, " - ", index)
# #hi
# #works