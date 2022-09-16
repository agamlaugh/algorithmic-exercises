cipher = {
    "a" : "z",
    "b" : "y",
    "c" : "x",
    "d" : "w",
    "e" : "v",
    "f" : "u",
    "g" : "t",
    "h" : "s",
    "i" : "r",
    "j" : "q",
    "k" : "p",
    "l" : "o",
    "m" : "n",
    "n" : "m",
    "o" : "l",
    "p" : "k",
    "q" : "j",
    "r" : "i",
    "s" : "h",
    "t" : "g",
    "u" : "f",
    "v" : "e",
    "w" : "d",
    "x" : "c",
    "y" : "b",
    "z" : "a",
    " " : " "
}
wordsToEncrypt = "hello my name is itamar"
def encrypter(word, cipher):
    encryptedString = ""
    for x in word:
        encryptedString = encryptedString + cipher[x]
    print(word)
    print(encryptedString)

encrypter(wordsToEncrypt, cipher)



# change each letter inside the strings to its corresponding value from the cipher 
#print the encrypted message/string
#return the encrypted string
#hello my name is itamar
# svool nb mznv rh rgznzi
#which key has this value





