print("Oct-30")


print("Linked list...")

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(545)
n2=Node(54)
n3=Node(55)
n4=Node(45)

n1.next=n2
n2.next=n3
n3.next=n4

head=n1

current=head

while current:
    print(current.data,end="->")
    current=current.next
print("Null")

