#preorder traversal of  the tree  root left right
class TreeNode :
    def __init__(self , value):
        self.value = value 
        self.left = None 
        self.right = None 
    

    
    
    
    
    
 
root = TreeNode(1)
root.left = TreeNode(2)
root.right  = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right= TreeNode(5)

    
    
def preorder_traversal(node):
    if node == None :
        return 
    
    print(node.value , end=" ")
    preorder_traversal(node.left )
    preorder_traversal(node.right)
      
        
preorder_traversal(root) 
     
root = TreeNode(1)
root.left = TreeNode(2)
root.right  = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right= TreeNode(5)
