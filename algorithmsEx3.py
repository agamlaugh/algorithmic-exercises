print('Enter maximum limit:')
maxLimit = int(input())
for number in range(1, maxLimit):
    numberStr = str(number)
    if numberStr.__contains__('7'):
        print('BOOM')
    elif number%7==0:
        print('BOOM')
    else:
        print(number)

#works