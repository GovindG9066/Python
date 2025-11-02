print("Nov-02")

print("Python Paper Pattern 2024")

print("1st question")

dict={
    "id":1, 
    "name":"Govind",
    "Address":"Pune",
    "Roll No":18
    }

print(dict.keys())

dict.update({"Age":21})

print(dict)

dict.pop("Address")

print(dict)

dict["name"]="Gondu"

print(dict)

print("2nd question")
text=input("Enter the value : ")
def swipe(text):
    char=list(text)

    for i in range(0,len(char)-1,2):
        char[i],char[i+1]=char[i+1],char[i]
        
    return "".join(char)

print(swipe(text))

print("3rd question : ")

names=['Ajay', 'Vijay', 'Ganesh', 'Paresh', 'Mahesh']

first=[name[0] for name in names]
print(first)