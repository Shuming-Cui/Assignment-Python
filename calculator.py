# calculator.py

def add(x, y):
    z = x + y
    print("{} + {} = {}".format(x, y, z))
    return z

def subtract(x, y):
    z = x - y
    print("{} - {} = {}".format(x, y, z))
    return z

def multiply(x, y):
    z = x * y
    print("{} * {} = {}".format(x, y, z))
    return z

def divide(x, y):
    z = x / y
    print("{} / {} = {}".format(x, y, z))
    return z

x = input("Enter a letter:")
print("You entered {}".format(x))

if x == "a":
    add(47, 7)
elif x == "s":
    subtract(47, 7)
elif x == "m":
    multiply(47, 7)
elif x == "d":
    divide(47.0, 7.0)
    

else:
    print("The {} is not recognized.".format(x))

print("Done")
