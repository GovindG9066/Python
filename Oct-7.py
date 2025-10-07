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

        