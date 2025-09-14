print("sept-14")

print("Armstrong Number : ")

num=int(input("Enter the number : "))
original=num
arm=0

while num != 0:
    digit=num % 10
    arm=arm+pow(digit,3)
    num//=10

if original== arm:
    print(original," is an armstrong number")
else:
    print(original," is not an armstrong number")


print("Palandrome number : ")

num=1223221
org=num
rev=0

while num != 0:
    digit=num % 10
    rev=rev*10+digit
    num//=10

if rev==org:
    print("palandrome number")
else:
    print("Not palandrome")

print("Prime Numbers : ")

num=4
check=0

for i in range(2,num):
    if num % i ==0:
        check+=1
        break

if check == 0:
    print("Prime Number")
else:
    print("Not Prime Number")
