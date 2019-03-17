# A set is a data type for mutable unordered collections of unique elements.
# Set is an unordered collection of unique items, so we cannot access them using index


numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)


number = [1, 1, 2, 3, 4]  # list
first = set(number)  # set
print(first)  # set removes repetitive items

second = {1, 3, 5}  # set is declared using curly braces

print(first | second)  # union of two sets
print(first & second)  # intersection of two sets
print(first - second)  # difference of two sets
print(first ^ second)  # symmetric difference of two sets

# Set remove duplicate elements
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a))
print(len(b))

# set does not support indexing

