def nameInput():
    print('What is your name?')
    name = input()
    return name

name = nameInput()
while name != 'exit':
    print('Welcome ', name)
    name = nameInput() 

#works