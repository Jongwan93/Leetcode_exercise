# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node): # node.value = 4
            # if current.left is None and current.right is None:
                # result.append(node.value)
                # return
            if not node:
                return
        
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        # # recurssion 
        # current = root
        # if current.left is None and current.right is None:
        #     result.append(current.value)
        # return result

        inorder(root)
        return result



        # [SOLUTION 2]
        # res = []
        # stack = []
        # cur = root

        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     res.append(cur.val)
        #     cur = cur.right

        # return res