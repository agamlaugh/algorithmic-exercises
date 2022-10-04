# create a loop that checks all number between 1 and 299
for number in range(1, 299):
    # store a variable to ensure that the values are integers. this way we can manipulate them as numbers(through operators and modifiers) to get a desired result
    numberStr = str(number)
    # check if number has a 3 in it. if so then print the number
    if numberStr.__contains__('3'):
        print(number)
    # check if number is divisible by 3. if so print it
    elif number%3==0:
        print(number)

#works