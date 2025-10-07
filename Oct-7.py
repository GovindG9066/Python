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