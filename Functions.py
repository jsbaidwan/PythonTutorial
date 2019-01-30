# functions to add integer number
def addition(x, y):
    return x + y


print(addition(2, 3))


# functions to add list
def increment(number, lit):
    return lit + number


print(increment([4], [1, 2]))


# Passing arguments

# passing list as argument
def add(lit):
    for ad in lit:
        return ad


print(add([3, 1, 8]))

# multiply the tuple


def multiply(*num):   # * is used to define it as tuple
    total = 1
    for x in num:
        total *= x
    return total


print(multiply(9, 2, 3))


