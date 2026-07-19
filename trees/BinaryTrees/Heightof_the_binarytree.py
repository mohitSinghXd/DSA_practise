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
root.right.right.left = TreeNode(9) 
root.right.right.right = TreeNode(10) 
root.right.right.right.right = TreeNode(11) 
  
  
  
def find_height_of_tree(node):
    if node == None:
        return 0 
    
    left_height = find_height_of_tree(node.left)
    right_height = find_height_of_tree(node.right)
    
    return max(left_height , right_height) + 1



height = find_height_of_tree(root)
print(height) 
 
 



  