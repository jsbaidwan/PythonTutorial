# Dictionary
print("Dictionary")

fruits = {"Apple": "Red", "Banana": "Yellow"}

print(fruits.items())
# print(fruits.items("Apple"))
print(fruits["Apple"])


fruits["kiwi"] = "Brown"  # update dictionary
print("Updated", fruits.items())

del fruits["Banana"]
print("Deleted", fruits.items())

