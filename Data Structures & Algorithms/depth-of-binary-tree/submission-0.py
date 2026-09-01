# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        if root.left:
            depth = max(self.maxDepth(root.left), depth)
        if root.right:
            depth = max(self.maxDepth(root.right), depth)
        return 1 + depth