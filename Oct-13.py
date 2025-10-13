print("Oct-13")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def traversal(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("Null")

def main():
    dll = LinkedList()

    # inserting nodes at beginning
    dll.insert_at_beginning(595)
    dll.insert_at_beginning(35)
    dll.insert_at_beginning(1)
    dll.insert_at_beginning(51)

    # traversal
    dll.traversal()

if __name__ == "__main__":
    main()
