# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1
        
        def maxDepth(root):
            if root == None:
                return 0
            L = maxDepth(root.left)
            R = maxDepth(root.right)
            self.ans = max(self.ans, L+R+1)
            return max(L,R) +1
        
        
        
        
        maxDepth(root)
        return self.ans - 1