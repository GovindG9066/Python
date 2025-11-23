print("Nov-23.py")

age="Govind"

try:
    if age>=18:
        print("You can vote")
    elif age < 18:
        print("You cant vote")
    else:
        print("Invalid age")

except TypeError:
    print("Type number format")