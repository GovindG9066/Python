print("Nov-12")

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Bst:
    def __init__(self):
        self.root=None

    def insertion(self,new_data):
        new_node=Node(new_data)
        if self.root is None:
            self.root=new_node
            return
        curr=self.root
        while True:
            if new_data < curr.data:
                if curr.left is None:
                    curr.left=new_node
                    break
                else:
                    curr=curr.left
            
            elif new_data > curr.data:
                if curr.right is None:
                    curr.right=new_node
                    break
                else:
                    curr=curr.right
            else:
                break

    # Inorder traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

if __name__=="__main__":
    

    bst=Bst()
    bst.insertion(12)
    bst.insertion(96)
    bst.insertion(4)
    bst.insertion(98)
    bst.insertion(25)

    bst.inorder(bst.root)
    print()
                