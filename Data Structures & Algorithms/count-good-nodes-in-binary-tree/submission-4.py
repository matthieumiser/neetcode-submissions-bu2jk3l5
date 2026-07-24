# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recurse(node, m):
            if not node:
                return 0
            count = 1 if node.val >= m else 0
            m = max(node.val, m)
            count += recurse(node.left, m)
            count += recurse(node.right, m)
            return count

        return recurse(root, root.val)