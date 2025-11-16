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