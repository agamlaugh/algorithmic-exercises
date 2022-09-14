for number in range(1, 299):
    numberStr = str(number)
    if numberStr.__contains__('3'):
        print(number)
    elif number%3==0:
        print(number)

#works