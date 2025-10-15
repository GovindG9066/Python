print("Oct-15")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSLL:
    def __init__(self):
        self.head = None

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def traversal(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                print("(Back to Head)")
                break

def main():
    CLL = CircularSLL()
    CLL.insert_at_end(5)
    CLL.insert_at_end(10)
    CLL.insert_at_end(15)
    CLL.traversal()

if __name__ == "__main__":
    main()
