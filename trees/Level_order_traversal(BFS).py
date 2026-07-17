# Level order Traversal 

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
root.right.left = TreeNode(8)
root.right.right= TreeNode(7)

    
    
def level_order_travershal(node):
    if node == None :
        return 
 
    inorder_traversal(node.left ) 
       
    print(node.value , end=" ") 
    
    inorder_traversal(node.right)
      
inorder_traversal(root) 
       
root = TreeNode(1)
root.left = TreeNode(2)
root.right  = TreeNode(3)
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5)
root.right.left= TreeNode(6)
root.right.right =TreeNode(7)
