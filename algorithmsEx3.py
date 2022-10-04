print('Enter maximum limit:')
# store a variable that will be the maximum limit the user inputs. make sure this input is an integer
maxLimit = int(input())
# create a for loop to loop through all the numbers up to the maximum limit that the user chose
for number in range(1, maxLimit):
    # make sure number is a string so it can be searched for as a character
    numberStr = str(number)
    # search for character 7. when found print boom
    if numberStr.__contains__('7'):
        print('BOOM')
    # create another if statement so that any number divisible by 7 also prints boom
    elif number%7==0:
        print('BOOM')
    else:
        print(number)

#works