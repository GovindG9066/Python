print("sept-23")

print("Dictionary : ")

dict={"Id":1,"name":"Govind","RollNo":18}
print(dict)

print(dict.keys()) # print all keyes
print(dict.values()) # print all values
print(dict.items()) # print items 

dict["Id"]=2
print(dict) # update id

dict["City"]="Pune"
print(dict)  # add a new key value pair

dict.pop("City")
print(dict)