# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_equal(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val != r2.val:
                return False
            return is_equal(r1.left, r2.left) and is_equal(r1.right, r2.right)

        ret = [False]
        def traverse(r, sr):
            if not r:
                return
            traverse(r.left, sr)
            traverse(r.right, sr)
            print(is_equal(r, sr))
            if is_equal(r, sr):
                ret[0] = True

        traverse(root, subRoot)
        return ret[0]
