print("Sept-12")

print("Leap Year : ")

year=2016

if year % 400 ==0 or year % 4==0 and year % 100 != 0:
    print("Yes it is leap year")
else:
    print("NO it is not leap year")


print("Rev String")
Str="Govind"

print(Str[::-1])

print("Star Patterns : ")

count=5

for i in range(1,count+1):
    print("* "*i)

print("Up side down Star Right angel triangle : ")

for i in range(count,0,-1):
    print("* "*i)

print("flip right angle triangle : ")

for i in range(1,count+1):
    print(" " * (count-i) + "*" * i)

