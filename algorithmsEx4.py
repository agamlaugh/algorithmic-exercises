import random
rNumber = random.randint(0,1000000)
print("random number is:" , rNumber)
n1 = 0
n2 = 1
fibNumber = n1 + n2
if rNumber == n1 or rNumber == n2:
    print(rNumber, 'is a fib number')
else:
    while fibNumber < rNumber:
        fibNumber = n1 + n2
        n1 = n2
        n2 = fibNumber
    if fibNumber == rNumber:
        print(rNumber, 'is a fib number')
    else:
        print(rNumber, 'is not a fib number')

#works