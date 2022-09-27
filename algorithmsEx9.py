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

cipher3_swap = {v: k for k, v in cipher3.items()}

print("Enter a phrase to decrypt:")
phrase = input()

def decrypter(word, cipher3_swap):
    decryptedString = "" 
    for x in word:
        decryptedString = decryptedString + cipher3_swap[x]
    return decryptedString

print(decrypter(phrase, cipher3_swap))

#works!!!!

#Good job!
# please have the function return the decrypted string and print that value.