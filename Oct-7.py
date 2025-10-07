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