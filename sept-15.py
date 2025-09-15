print("sept-15")
print("Factorial Using while loop incremental: ")

num=5
count=1
output=1
while count <= num:
    output=output*count
    count+=1
print(output)

print("factorial using while loop decremental: ")

num=5
op=1
while num != 0:
    op=op*num
    num-=1
print(op)

print("Factorial using for loop incremental : ")

num=5
op=1
for  i in range (1,num+1):
    op=op*i
print(op)

print("factorial using for loop decremental : ")

num=5
op=1

for i in range(num,0,-1):
    op=op*i
print(op)

print("Factorial using recursion : ")
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5)) 
