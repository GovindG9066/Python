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