print("Dec-5")
print("File Handling")


try:
    file=open("tex3t.txt","r")
    print("File is Found...")
    print("This is the content of the file \n")
    print(file.read())
    file.close()
except FileNotFoundError as e:
    print("Error 404...")
    print("Error : ",e)
    print("This File is not exits")
except:
    print("Some Thing Went Wrong")

finally:
    print("And All Set")

