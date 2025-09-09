print("hello")

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