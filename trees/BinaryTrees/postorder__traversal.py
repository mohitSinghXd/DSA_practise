# postorder traversal means left  right root 

class TreeNode :
    def __init__(self , value):
        self.value = value 
        self.left = None 
        self.right = None 
    

root = TreeNode(1)
root.left = TreeNode(2) 
root.right  = TreeNode(3)
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5)
root.right.left= TreeNode(6) 
root.right.right= TreeNode(7)

    
    
def postorder_traversal(node):
    if node == None :
        return 
 
    postorder_traversal(node.left ) 
    postorder_traversal(node.right) 
    print(node.value , end=" ")  
      
postorder_traversal(root) 
     
root = TreeNode(1)
root.left = TreeNode(2)
root.right  = TreeNode(3)
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5)
root.right.left= TreeNode(6)
root.right.right =TreeNode(7)
