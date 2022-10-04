import random
# store random value as a variable
rNumber = random.randint(0,1000000)
print("random number is:" , rNumber)
# store the first numbers in a fibonacci sequence
n1 = 0
n2 = 1
# create the fibonacci pattern and store it in a variable
fibNumber = n1 + n2
#check to see if the random number is equal to the first two numbers in the fib sequence
if rNumber == n1 or rNumber == n2:
    print(rNumber, 'is a fib number')
else:
    # create a loop that will run unless the fib number is less than the random number
    while fibNumber < rNumber:
        # create the pattern that makes up a fib number
        fibNumber = n1 + n2
        n1 = n2
        n2 = fibNumber
    # check if the random number is a fib number
    if fibNumber == rNumber:
        print(rNumber, 'is a fib number')
    else:
        print(rNumber, 'is not a fib number')

#works