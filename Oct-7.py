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