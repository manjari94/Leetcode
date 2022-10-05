# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxl = 0
        maxr = 0
        if root is None:
            return 0
        else:
            maxl = 1+self.maxDepth(root.left)
            maxr = 1+self.maxDepth(root.right)
        return max(maxl,maxr)
