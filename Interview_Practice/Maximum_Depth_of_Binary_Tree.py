# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        def findMaxDepth(node, depth):
            if node.left is None and node.right is None:
                return depth
            left = findMaxDepth(node.left, depth + 1) if node.left else 0
            right = findMaxDepth(node.right, depth + 1) if node.right else 0

            return max(left, right)
        
        return findMaxDepth(root, 1)