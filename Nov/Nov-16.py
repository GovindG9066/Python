print("Nov-16")

print("Armstrong Number :")

num=153
original=num
arm=0
while num:
    digit=num%10
    arm+=pow(digit,3)
    num=num//10

if original==arm:
    print("Arm")
else:
    print("Not Arm")