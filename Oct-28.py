print("Oct-28")



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def traversal(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

def main():
    ll = LinkedList()
    ll.insert_at_end(15)
    ll.insert_at_end(20)
    ll.insert_at_end(25)
    ll.traversal()

if __name__ == "__main__":
    main()
