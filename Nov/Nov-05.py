print("Nov-05")

print("Star pattern : ")
count=5
for i in range(count+1):
    print("  " * (count-i) + "* " * i)

print("Star Pattern up side down flip right angle triangle : ")

for i in range(count+1):
    print("  " * i +"* " * (count-i))

count = 5
for i in range(1, count+1):
    # Spaces before the first star
    print("  " * (count-i) + "* " + "  " * (i-1))
