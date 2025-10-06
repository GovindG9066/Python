print("sept-6")
first=int(input("Enter the first number :"))
second=int(input("Enter the second number : "))
print("Operator + - * / %")
oper=input("Enter the Operator : ")
print("calculator using switch :")

def calculator(a,b,oper):
    match oper:
        case "+":
            print("addition is  : ")
            return a+b
        case "-":
            print("Subtraction is : ")
            return a-b
        case "*":
            print("Multiplication is : ")
            return a*b
        case "/":
            if b==0:
                print("0 not allowed to divide")
            else:
                print("Division is :")
                return a/b
        case "%":
            print("Reminder is : ")
            return a%b
        

answer=calculator(first,second,oper)
print(answer) 