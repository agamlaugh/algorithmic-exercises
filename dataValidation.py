def multiple(x, y):
    try:
        x = int(x)
    except:
        raise Exception("error: ", x, "is not an integer")

    try:
        y = int(y)
    except:
        raise TypeError("error: ", y, "is not an integer")

    result = x * y 
    return result

res1 = multiple(3, "hellooooo")

res2 = multiple(res1, 3)

print(res1)
print(res2)
