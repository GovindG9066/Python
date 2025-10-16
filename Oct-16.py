print("Oct-16")

print("Pyramid triangle : ")
count=5
for i in range(1,count+1):
    print("  " * (count-i) + "* " * i + "* " * (i-1))

print("Up side down Pyramid Triangle :")

count = 5  # define number of rows

for i in range(count, 0, -1):
    print("  " * (count - i) + "* " * (2 * i - 1))
