print("Nov-13")

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BS:
    def __init__(self):
        self.root=None
    
    def insert(self,new_data):
        new_node=Node(new_data)
        if self.root is None:
            self.root=new_node
            
        curr=self.root
        while True:
            if new_data<curr.data:
                if curr.left is None:
                    curr.left=new_node
                    break
                else:
                    curr=curr.left
            elif new_data > curr.data:
                if curr.right is None:
                    curr.right=new_node
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
    bts=BS()
    bts.insert(25)
    bts.insert(22)
    bts.insert(635)
    bts.insert(225)
    bts.insert(2)

    bts.inorder(bts.root)
    print()