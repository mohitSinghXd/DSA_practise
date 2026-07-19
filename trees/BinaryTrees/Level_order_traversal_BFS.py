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

    
def level_order_travershal(node):
    if node == None :
        return  
    
    result  = [] 
    queue = deque() 
    queue.append(node) 
    while len(queue)!= 0:
        e = queue.popleft()
        result.append(e.data) 
        if e.left is not None :
            queue.append(e.left) 
        if e.right is not None:
            queue.append(e.right)
    
    return root
    
