print("sept-25")

print("learning sets in python : ")

my_set={4,8,6,8,64,954,4}
print(my_set)

print("add new items in set : ")

fruits={"mango","orange","apple","banana"}
print(fruits)
print(type(fruits))
fruits.add("cherry")
print(fruits)

fruits.remove("apple")
print(fruits)

print("Set operations :")
num1={7,8,8,4,6,8,5,5,5}
num2={6,7,6,4,8,2,16,41}

print(num1)
print(num2)

print(num1 | num2) # print all the items in both sets also remove duplicate

print(num1 & num2) # print the intersection in (same in both sets)

print(num1 - num2) # items which in num 1 but not in num 2
print(num2 - num1) # items which in num 2 but not in num 1 (differencieate)

print(num1 ^ num2) # items which are difference in both 

print("Useful methods :")
abc={88,55,66,44,99,455,66,55,6}
print(len(abc)) # count the length of the set not count the duplicate

print(66 in abc)
print(10 not in abc)

print("Remove all the items in set : ")
abc.clear()
print(abc)