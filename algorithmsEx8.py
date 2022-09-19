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

def encrypter(word, cipher3):
    encryptedString = ""
    for x in word:
        encryptedString = encryptedString + cipher3[x]
    print(word)
    print(encryptedString)

encrypter(phrase, cipher3)

#works
