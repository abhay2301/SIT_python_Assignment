class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
        
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
            self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        elif data<root.item:
            root.left=self.rinsert(root.left,data)
        elif data>root.item:
            root.right=self.rinsert(root.right,data)
                
        return root
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.item,end=' -> ')
            self.inorder(root.right)


bst=BST()
bst.insert(60)
bst.insert(30)
bst.insert(70)          
bst.inorder(bst.root)