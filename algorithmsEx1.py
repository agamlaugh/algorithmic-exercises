# create a function that asks what your name is, accepts input, and returns it
def nameInput():
    print('What is your name?')
    name = input()
    return name

#call the funtion and store it under a variable
name = nameInput()
# create a while loop so that unless the name is exit, 
# the user is greeted with their name input.
while name != 'exit':
    print('Welcome ', name)
    # the loop continues to ask for another name until condition is met
    name = nameInput() 

#works