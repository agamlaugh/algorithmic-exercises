# create a function that asks what your name is, accepts input, and returns it
def nameInput():
    print('What is your name?')
    name = input()
    return name

# create a function to change output if name is exit
def exitChecker(name):
    # create a while loop so that unless the name is exit, 
    # the user is greeted with their name input.
    while name != 'exit':
        print('Welcome ', name)
        # the loop continues to ask for another name until condition is met
        name = nameInput() 

#call the funtion and store it under a variable
name = nameInput()

# call the function
exitChecker(name)

# send input and output history to new file
f = open("/Users/meytallitmanovitz/coding/algorithmic-exercises/algorithmsEx1outputs.txt", "a")
f.write(f"{name} --> {exitChecker(name)}\n")
f.close()