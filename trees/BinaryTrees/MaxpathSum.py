# Level Order Traversal + Maximum Path Sum

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Creating Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)
root.right.right.right = TreeNode(10)
root.right.right.right.right = TreeNode(11)


maxi = float("-inf")


def max_path_sum(root):
    global maxi

    if root is None:
        return 0

    leftSum = max_path_sum(root.left)
    if leftSum < 0:
        leftSum = 0

    rightSum = max_path_sum(root.right)
    if rightSum < 0:
        rightSum = 0

    # Update maximum path sum
    maxi = max(maxi, leftSum + rightSum + root.value)

    # Return best path to parent
    return root.value + max(leftSum, rightSum)


max_path_sum(root)
print("Maximum Path Sum:", maxi)