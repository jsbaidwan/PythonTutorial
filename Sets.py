# Set is an unordered collection of unique items, so we cannot access them using index

number = [1, 1, 2, 3, 4]  # list
first = set(number)  # set
print(first)  # set removes repetitive items

second = {1, 3, 5}  # set is declared using curly braces

print(first | second)  # union of two sets
print(first & second)  # intersection of two sets
print(first - second)  # difference of two sets
print(first ^ second)  # symmetric difference of two sets

# set does not support indexing

