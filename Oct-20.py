print("X pattern using stars :")

count=5

for i in range(count):
    print(("  " * i + "* " + "  " * (count-i-1)) + ("  " * (count-i-1) + "* "   ))
for i in range(count):
    print(("  " * (count-i-1) + "* " + "  " * i)+("  " * i + "* "))