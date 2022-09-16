#create a cfunction that recieves a list of numbers and a number and returns the position of the value in that list (index location) Ex. 1,2,3,4,5, where is 4 located, 3

def numberIndex(numList, number):
    counter = 0
    while counter < len(numList):
        if numList[0] == number: 
            return counter


        
index = numberIndex([1,2,3,4,5], 4)
print("Index of number is:", index)
