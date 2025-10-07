print("Oct-7")

print("Instance variable :")

class Mywork:
    def disp(self):
        print("I am the instance method")
    
def main():
    print("Inside the main method")
    obj=Mywork()
    obj.disp()
    print("End of main")

if __name__=="__main__":
    main()
    print("End of application")


class demo:
    def __init__(self):
        print("I am the constructor...")
    def __del__(self):
        print("Inside distructor...")

def main():
    print("Inside main function...")
    obj=demo()
    print("End of the main method...")
if __name__=="__main__":
    main()
    print("End of the program")


print("Practice from chatgpt...")
print("Question 1st")
class laptop:
    def showBand(self,bandName):
        self.bandName=bandName
        print("Showing band...")
        print(self.bandName)
lap=laptop()
lap.showBand("b1")

print("Question 2nd : ")

class student1:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
std=student1("Govind",21)
std.display()  

print("3rd question : ")
class car1:
    def __init__(self,modal,price):
        self.modal=modal
        self.price=price
    
obj1=car1("Thar",2000000)
print(obj1.modal)
obj2=car1("Porshar",30000000)
print(obj2.modal)

print("4th Question : ")
class demo2:
    def __init__(self):
        print("I am the constructor...")
    def __del__(self):
        print("I am distructor...")
forth=demo2()

print("5th question ---tricky---")

class emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def bonus(self):
        self.percent=self.sal*(10/100)
        self.total=self.sal+self.percent
        print(f"Total salary with bonus is :{self.total}")

e1=emp("Krishna",100)
e1.bonus()

print("Question 6th start : ")
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    
cal=Calculator(15,6)
print(f"First Number : {cal.a}")
print(f"Second Number : {cal.b}")

print(f"Addition : {cal.add()}")
print(f"Subtraction : {cal.sub()}")
print(f"Multiplication : {cal.mul()}")

print("LinkedList Start : ")

class LinkedList:
    def __init__(self,data):
        self.data=data
        self.next=None
    
n1=LinkedList(15)
n2=LinkedList(16)
n3=LinkedList(35)
n4=LinkedList(9)
n5=LinkedList(19)


n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

head=n1

current=head

while current:
    print(current.data)
    current=current.next
print("None")


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(25)
n2=Node(50)
n3=Node(75)
n4=Node(100)

n1.next=n2
n2.next=n3
n3.next=n4

head=n1

current=head

while current:
    print(current.data,end="->")
    current=current.next
print("None")

print("Searching element in the linkedlist :")

class Node2:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node2(56)
n2=Node2(5)
n3=Node2(5686)
n4=Node2(5674)

n1.next=n2      
n2.next=n3      
n3.next=n4

head=n1


def search(head,key):
    current=head
    while current:
        if current.data==key:
            print("Mil gyi")
            return True
        else:
            current=current.next
        return False

key = 5
if search(head, key):
    print(f"{key} found in linked list")
else:
    print(f"{key} not found in linked list")
