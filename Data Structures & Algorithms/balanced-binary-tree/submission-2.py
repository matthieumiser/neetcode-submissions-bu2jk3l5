# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        balanced = True
        def recurse(curr, depth):
            nonlocal balanced
            if not curr or depth == -1:
                return depth
            depth += 1
            depth_left = recurse(curr.left, depth)
            depth_right = recurse(curr.right, depth)
            depth = max(depth_left, depth_right)
            if abs(depth_left - depth_right) > 1:
                balanced = False
            return depth
        recurse(root, 0)
            
        return balanced
            
            