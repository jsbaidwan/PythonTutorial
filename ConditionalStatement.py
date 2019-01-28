
# If condition

age = 22
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

print("done")

# Statement block
if age > 1:
    pass   # for empty block use pass
else:
    pass

# Not Operators
name = "baidwan"
if not name:
    print("Not a name")

# And Operators
age = 22
if age >= 18 and age < 60:
    print("Eligible")
# Chain comparison
if 18 <= age < 60:
    print("eligible")


if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

# Ternary Operators for above Statement

message = "Eligible " if age >= 18 else "Not Eligible"

print(message)

