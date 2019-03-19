# A dictionary is a mutable data type that stores mappings of unique keys to values.
print("Dictionary")

fruits = {"Apple": "Red", "Banana": "Yellow"}

print(fruits.items())
# print(fruits.items("Apple"))
print(fruits["Apple"])


fruits["kiwi"] = "Brown"  # update dictionary
print('Updated', fruits.items())

del fruits["Banana"]
print('Deleted', fruits.items())

print("Check for kiwi key value: ", 'kiwi' in fruits)

# loop
for i, j in fruits.items():
    print(i, j)


def foo(x=[]):
    x.append(1)
    print(x)


foo()
foo()
foo()
