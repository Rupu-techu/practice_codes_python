class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    if (root):
        inorder(root.left) 
        print(root.data,end=" ")
        inorder(root.right)
def preorder(root):
    if(root):
        preorder(root.left)
        preorder(root.right)
        print(root.data,end=" ")
def postorder(root):
    if(root):
        print(root.data,end=" ")
        postorder(root.left)
        postorder(root.right)
            
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)

print("inorder:")
inorder(root)
print("\n")

print("preorder:")
preorder(root)
print("\n")

print("postorder:")
postorder(root)
print("\n")
