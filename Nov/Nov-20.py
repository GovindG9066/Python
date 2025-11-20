# Singly Linked List Implementation in Python

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Insert after a specific value
    def insert_after(self, prev_data, data):
        temp = self.head
        while temp and temp.data != prev_data:
            temp = temp.next
        if not temp:
            print("Node with data", prev_data, "not found.")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # Delete a node by value
    def delete_node(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # If key not found
        if not temp:
            print("Node with data", key, "not found.")
            return

        # Unlink the node
        prev.next = temp.next
        temp = None

    # Search for a node
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # Print the entire linked list
    def display(self):
        temp = self.head
        if not temp:
            print("Linked list is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Driver code
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_beginning(5)
    sll.insert_after(10, 15)

    print("Linked List:")
    sll.display()

    print("\nSearch 15:", sll.search(15))
    print("Search 25:", sll.search(25))

    print("\nDeleting node with value 10...")
    sll.delete_node(10)

    print("Updated Linked List:")
    sll.display()