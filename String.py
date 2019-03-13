# single quotes
print('This is Python course')
# double quotes
print("This is Python course")

# Triple quotes for multiple lines
print("""This
is the 
Python Course""")

# Escape the single quotes
print("Doesn't know")
print('Doesn\'t know')

# New line
print("First line \n Second line")

# Escape the double quotes
print('"Yes", he said')
print("\"Yes\", he said")

print('Py' 'charm')

# String concatenate and repeated
print(2 * "ass" + "ination")

course_name = "Python Tutorial"
print(course_name)

# length of the string
print(len(course_name))

# Character at first index
print(course_name[0])

# Character at second last index
print(course_name[-1])

# First three character
print(course_name[0:3])
print(course_name[:3])

# First to last character
print(course_name[0:])
print(course_name[:])

# Immutable properties of String
print(id(course_name))
print(id(course_name[0]))

# Formatted String
formatting = f"{len(course_name)} {2+1}"
print(formatting)

# String methods
# Character Capitalize
print(course_name.capitalize())

# Character to lowercase
print(course_name.lower())

# First character of every word be capital
print(course_name.title())

# Remove the white space
print(course_name.strip())

# Find character of word
print(course_name.find("thon"))

# Replace character
print(course_name.replace("P", "-"))

# Check existence nonexistence
print("Tutorial" in course_name)
print("Tutorial" not in course_name)

# using count method in the string
print("One fish, Two fish, blue fish, red fish".count('fish'))
