# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, out = deque([root]), []
        while queue:
            nodes = []
            while queue:
                nodes.append(queue.popleft())
            out.append([x.val for x in nodes])
            for node in nodes:
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return out