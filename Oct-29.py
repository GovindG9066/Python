print("Oct-29")

print("Armstrong Number :")

num=153
original=num
arm=0
while num:
    digit=num % 10
    arm+=pow(digit,3)
    num=num//10

if original==arm:
    print("Armstrong")
else:
    print("Not armstrong")
