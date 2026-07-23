# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse(node):
            if node.val == p.val or node.val == q.val:
                return node
            elif min(p.val, q.val) < node.val < max(p.val, q.val):
                return node
            
            if p.val < node.val:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(root)