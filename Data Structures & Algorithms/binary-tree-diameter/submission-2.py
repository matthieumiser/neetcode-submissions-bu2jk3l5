# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sumz = []
        def recurse(curr, max_depth, sums):
            if curr == None:
                return max_depth, sums
            max_depth += 1
            left_depth, _ = recurse(curr.left, 0, sums)
            right_depth, _ = recurse(curr.right, 0, sums)
            max_depth += max(left_depth, right_depth)
            sums.append(left_depth + right_depth)
            
            return max_depth, sums
        r = recurse(root, -1, sumz)
        return max(sumz)