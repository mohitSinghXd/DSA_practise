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
root.right.right= TreeNode(7)
root.right.right.left = TreeNode(9) 
root.right.right.right = TreeNode(10) 
root.right.right.right.right = TreeNode(11) 
  
  
  
def isTree_balanced(node):
    if node == None:
        return 0 
    
    left_height =isTree_balanced(node.left)  
    if left_height == -1 :
        return -1
    
    right_height =isTree_balanced(node.right)
    if  right_height == -1:
        return -1
    
    if abs(left_height -right_height) > 1:
        return -1 
    
    return max(left_height , right_height) + 1



height =isTree_balanced(root)
if height == -1 :
    print(False)
else :
    print(True)
 
 



  