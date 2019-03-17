# Data structures are containers that organize and group data types together in different ways.
# A list is one of the most common and basic data structures in Python.

list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0])

print(list_of_random_things[-1])

print(list_of_random_things[-2])


# use list indexing to determine the number of month with 31 days
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
num_days = days_in_month.count(31)
print(num_days)

# join method
new_str = "-".join(["fore", "aft", "starboard", "port"])
print(new_str)

# join and sorting
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))


# A tuple is another useful container.
# It's a data type for immutable ordered sequences of elements.
# They are often used to store related pieces of information.

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))

