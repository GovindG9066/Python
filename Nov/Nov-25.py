A=[12,4,6,65,5,2,6,3]
n=len(A)

small=A[0]
Large=A[0]

for i in range(1,n):
    if small > A[i]:
        small,A[i]=A[i],small
    if Large < A[i]:
        Large,A[i]=A[i],Large

print(A)
print(f"Small element in the given array is : {small}")
print(f"Large element in the given array is : {Large}")


print("Sinlgy LinkedList")
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    
    def insert(self,new_data):
        new_node=Node(new_data)

        if self.head is None:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
    def traversal(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print("None")

if __name__=="__main__":
    ll=LL()
    ll.insert(20)
    ll.insert(10)
    ll.insert(220)
    ll.insert(201)
    ll.traversal()
