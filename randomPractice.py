f = open("algorithmsEx6outputs.txt", "a")
f.write("hello")
f.close()

f = open("algorithmsEx6outputs.txt", "r")
print(f.read())
f.close()