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

print("Palandrom Number : ")

num1=1502051
ori=num1
rev=0
while num1:
    digit=num1 % 10
    rev=rev*10+digit
    num1=num1//10

if ori==rev:
    print("Palandrom")
else:
    print("Not Palandrom")
