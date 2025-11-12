class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Binary:
    def __init__(self):
        self.root=None

    def insert(self,new_data):
        new_node=Node(new_data)
        if self.root is None:
            self.root=new_node

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
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

if __name__=="__main__":
    bt=Binary()
    bt.insert(50)
    bt.insert(5)
    bt.insert(10)
    bt.insert(56)
    bt.insert(90)

    bt.inorder(bt.root)
    print()

                
                    