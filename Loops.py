# For loops

# Iterate over String
for x in ("Pyth"):
    print(x)

# Iterate over List
for x in ('o', 'n'):
    print(x)

# Range function
# Range function does not return list, its an object

# class range(stop)
for x in range(5):
    print(x)

# class range(start, stop)
for x in range(2, 5):
    print(x)

# class range(start, stop[, step])
# step as increment in loop
for x in range(0, 10, 2):
    print(x)

# For else
# Look for word starting with j

name = ["john", "Mike"]
for names in name:
    if names.startswith("j"):
        print("Found")
        break   # to break the loop
# It will be only used if loop successfully complete without using break
else:
    print("Not found")

# While
# loop stop as soon as guess matches the answer

answer = 5
guess = 0

while answer != guess:
    guess = int(input("Guess: "))
# else will execute if loop will successfully complete without using break statement
else:
    pass

