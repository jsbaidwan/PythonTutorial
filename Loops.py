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
name = ["john", "Mike"]
for names in name:
    if names.startswith("j"):
        print("Found")
        break   # to break the loop
else:
    print("Not found")
