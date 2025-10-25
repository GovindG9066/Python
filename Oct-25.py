print("Oct-25")

print("Star Pattern")

count=5

for i in range(1,count+1):
    print("* " * i)

print("")

for i in range(1,count+1):
    print("* " * (count+1-i))

print("")

for i in range(count+1):
    print("  " * i + "* " * (count-i))

print("")

for i in range(count+1):
    print("  " * (count-i) + "* " * i)

print("")

for i in range(count+1):
    print(" " * (count-i) + "* " * i )

print("")

for i in range(count+1):
    print(" " * i + "* " * (count-i))


print("X pattern using stars :")

count=5

for i in range(count):
    print(("  " * i + "* " + "  " * (count-i-1)) + ("  " * (count-i-1) + "* "   ))
for i in range(count):
    print(("  " * (count-i-1) + "* " + "  " * i)+("  " * i + "* "))