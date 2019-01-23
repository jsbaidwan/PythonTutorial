# Integer, boolean, string, float, tuple, frozenset are Immutable
# List, set, dictionary are mutable

# Integer are Immutable, original memory location cannot be overwritten
x = 1
# Address of memory location
print(id(x))


x = x + 1
print(id(x))

# List are mutable, memory location is overwritten
y = [1, 5, 3]
print(id(y))

y.append(4)
print(id(y))

