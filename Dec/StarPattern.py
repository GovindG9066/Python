print("Simple Star Pattern :")

count=5

for i in range(1,count+1):
    print("* "*i)

print("Up Side Down Simple Star Pattern :")

for i in range(1,count+1):
    print("* " * (count+1-i))


print("Simple flip right angle triangle : ")

for i in range(1,count+1):
    print("  "*(count-i)+"* " *i)