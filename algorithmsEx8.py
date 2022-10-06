# create a dictionary 
cipher3 = {
    "a" : "d",
    "b" : "e",
    "c" : "f",
    "d" : "g",
    "e" : "h",
    "f" : "i",
    "g" : "j",
    "h" : "k",
    "i" : "l",
    "j" : "m",
    "k" : "n",
    "l" : "o",
    "m" : "p",
    "n" : "q",
    "o" : "r",
    "p" : "s",
    "q" : "t",
    "r" : "u",
    "s" : "v",
    "t" : "w",
    "u" : "x",
    "v" : "y",
    "w" : "z",
    "x" : "a",
    "y" : "b",
    "z" : "c",
    " " : " "
}

print("Enter a phrase to encrypt:")
phrase = input()

# Please have the function return the encrypted string and print that value. 
# look at functions in the return section in w3 schools

# create a function to encrypt a phrase based on the dictionary created
def encrypter(phrase, cipher3):
    encryptedString = ""
    # loop through through each character in the phrase, encrypt it, and add it to the list of strings(phrase)
    for x in phrase:
        encryptedString = encryptedString + cipher3[x]
    # return encrypted string
    return encryptedString

print(encrypter(phrase, cipher3))

#works
