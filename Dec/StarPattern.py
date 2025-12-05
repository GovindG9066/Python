print("Simple Star Pattern :")

count=5

for i in range(1,count+1):
    print("* "*i)

print("Up Side Down Simple Star Pattern :")
c=count+1
for i in range(1,c):
    print("* " * (c-i))


print("Simple flip right angle triangle : ")

for i in range(1,count+1):
    print("  "*(count-i)+"* " *i)

print("Up Side Down flip Right angle trangle :")

for i in range(1,count+1):
    print("  " * i + "* " * (count+1-i))

print("Triangle pattarn without diagonal :")

for i in range(1,count+1):
    print(" " * (count+1-i) + "* " * i )

print("Up Side Down Triangle Pattern Without diagonal :")

for i in range(1,count+1):
    print(" " * i + "* " * (count+1-i))