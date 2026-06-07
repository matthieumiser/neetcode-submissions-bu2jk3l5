# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recurse(curr, max_depth, sums):
            if curr == None:
                return max_depth, sums
            max_depth += 1
            left_depth, left_sum = recurse(curr.left, 0, sums)
            right_depth, right_sum = recurse(curr.right, 0, sums)
            max_depth += max(left_depth, right_depth)
            sums = max(sums, left_sum, right_sum, left_depth + right_depth)
            
            return max_depth, sums
        _, sumz = recurse(root, -1, 0)
        return sumz