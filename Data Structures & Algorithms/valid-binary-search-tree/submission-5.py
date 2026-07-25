# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, mx, mn):
            print(mx, mn)
            if not node:
                return True
            if node.val >= mx or node.val <= mn:
                return False
            return dfs(node.left, min(mx, node.val), mn) and dfs(node.right, mx, max(mn, node.val))
        return dfs(root, float("inf"), -float("inf"))