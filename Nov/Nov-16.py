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


print("Sum of square of first n natural numbers :")



def Sum_of_Square(num1):
    sum=0
    for i in range(1,num1+1):
        print(f"power of {i} is = {pow(i,2)}")
        sum+=pow(i,2)
    print(f"sum of square of first n natural number is :{sum}")  

Sum_of_Square(5)

print("Check prime num or not")

def prime(p1):
    pn=0
    for i in range(2,p1):
        if p1 % i == 0:
            pn+=1
            break
        else:
            pn=0
    if pn == 0:
        print(f"Given Number {p1} is Prime")
    else:
        print(f"Given Number {p1} is NOT Prime")

prime(13)