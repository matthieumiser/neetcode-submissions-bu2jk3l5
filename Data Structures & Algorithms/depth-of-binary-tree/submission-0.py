# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurse(root, depth):
            if not root:
                return depth
            depth += 1
            depth = max(recurse(root.left, depth), recurse(root.right, depth))
            return depth
        return recurse(root, 0)