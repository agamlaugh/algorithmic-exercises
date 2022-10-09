# create a function that prints any number with or divisible by 3 between a ceratin range
def number3Checker():
    # create a loop that checks all number between 1 and 299
    for number in range(1, 299):
        # store a variable to make the number a string. 
        # this way the number can be searched for like a character
        numberStr = str(number)
        # check if number has a 3 in it. if so then print the number
        if numberStr.__contains__('3'):
            print(number)
        # check if number is divisible by 3. if so print it
        elif number%3==0:
            print(number)

# call the function that checks for 3
number3Checker()




















# # create a loop that checks all number between 1 and 299
# for number in range(1, 299):
#     # store a variable to make the number a string. 
#     # this way the number can be searched for like a character
#     numberStr = str(number)
#     # check if number has a 3 in it. if so then print the number
#     if numberStr.__contains__('3'):
#         print(number)
#     # check if number is divisible by 3. if so print it
#     elif number%3==0:
#         print(number)

