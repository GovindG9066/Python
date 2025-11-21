# ------------------------------------
# Node class
# ------------------------------------
class Node:
    def __init__(self, data):
        self.data = data        # Value of the node
        self.prev = None        # Pointer to previous node
        self.next = None        # Pointer to next node

# ------------------------------------
# Doubly Linked List class
# ------------------------------------
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # -----------------------------
    # Insert a node at the beginning
    # -----------------------------
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # -----------------------------
    # Insert a node at the end
    # -----------------------------
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # -----------------------------
    # Insert after a given value
    # -----------------------------
    def insert_after(self, key, data):
        temp = self.head
        while temp is not None and temp.data != key:
            temp = temp.next
        if temp is None:
            print("Node with value", key, "not found.")
            return
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node

    # -----------------------------
    # Delete a node from the beginning
    # -----------------------------
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # -----------------------------
    # Delete a node from the end
    # -----------------------------
    def delete_from_end(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None

    # -----------------------------
    # Delete a node by value
    # -----------------------------
    def delete_by_value(self, key):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        temp = self.head
        # If the node to delete is the head
        if temp.data == key:
            self.delete_from_beginning()
            return
        while temp is not None and temp.data != key:
            temp = temp.next
        if temp is None:
            print("Node with value", key, "not found.")
            return
        # If it's the last node
        if temp.next is None:
            temp.prev.next = None
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

    # -----------------------------
    # Search for a node
    # -----------------------------
    def search(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # -----------------------------
    # Display list forward
    # -----------------------------
    def display_forward(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            last = temp
            temp = temp.next
        print("None")

    # -----------------------------
    # Display list backward
    # -----------------------------
    def display_backward(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next  # Go to last node
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

# ------------------------------------
# Example Usage
# ------------------------------------
if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("\nInserting at beginning:")
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(5)
    dll.display_forward()

    print("\nInserting at end:")
    dll.insert_at_end(20)
    dll.insert_at_end(25)
    dll.display_forward()

    print("\nInsert after 10:")
    dll.insert_after(10, 15)
    dll.display_forward()

    print("\nDelete from beginning:")
    dll.delete_from_beginning()
    dll.display_forward()

    print("\nDelete from end:")
    dll.delete_from_end()
    dll.display_forward()

    print("\nDelete node with value 15:")
    dll.delete_by_value(15)
    dll.display_forward()

    print("\nDisplay backward:")
    dll.display_backward()

    print("\nSearch for 20:", dll.search(20))
    print("Search for 100:", dll.search(100))