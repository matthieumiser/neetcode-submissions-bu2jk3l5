# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count = 0
        def recurse(node, m):
            nonlocal good_count
            if not node:
                return
            if node.val >= m: good_count += 1
            new_m = max(m, node.val)
            recurse(node.left, new_m)
            recurse(node.right, new_m)
        recurse(root, root.val)
        return good_count