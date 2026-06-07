# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(curr):
            if not curr:
                return 0
            left = recurse(curr.left)
            if left == -1:
                return -1
            right = recurse(curr.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1
            
        return recurse(root) != -1
            
            