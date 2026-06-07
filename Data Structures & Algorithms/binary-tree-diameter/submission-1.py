# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sums = []
        def recurse(curr, max_depth):
            if curr == None:
                return max_depth
            max_depth += 1
            left_depth = recurse(curr.left, 0)
            right_depth = recurse(curr.right, 0)
            max_depth += max(left_depth, right_depth)
            sums.append(left_depth + right_depth)
            
            return max_depth
        r = recurse(root, -1)
        return max(sums)