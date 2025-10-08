print("Oct-8")

print("Linked list traversal...")

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(56)
n2=Node(5)
n3=Node(556)
n4=Node(65)

n1.next=n2
n2.next=n3
n3.next=n4

head=n1

def traversal(head):
    current=head
    while current:
        print(current.data,end="->")
        current=current.next
    print("Null")

traversal(head)
