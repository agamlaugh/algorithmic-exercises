# create a function that prints boom instead of 7 or a number divisible by 7
def number7Finder():
    # create a for loop to loop through all the numbers up to the maximum limit that the user choose
    for number in range(1, maxLimit):
        # make sure number is a string so it can be searched for as a character
        numberStr = str(number)
        # search for character 7 and when found print boom
        if numberStr.__contains__('7'):
            print('BOOM')
        # create another if statement so that any number divisible by 7 also prints boom
        elif number%7==0:
            print('BOOM')
        else:
            print(number)


print('Enter maximum limit:')
# store a variable that will be the maximum limit the user inputs. 
# make sure this input is an integer
maxLimit = int(input())

# call the function
number7Finder()



































# print('Enter maximum limit:')
# # store a variable that will be the maximum limit the user inputs. 
# # make sure this input is an integer
# maxLimit = int(input())
# # create a for loop to loop through all the numbers up to the maximum limit that the user chose
# for number in range(1, maxLimit):
#     # make sure number is a string so it can be searched for as a character
#     numberStr = str(number)
#     # search for character 7. when found print boom
#     if numberStr.__contains__('7'):
#         print('BOOM')
#     # create another if statement so that any number divisible by 7 also prints boom
#     elif number%7==0:
#         print('BOOM')
#     else:
#         print(number)

# #works