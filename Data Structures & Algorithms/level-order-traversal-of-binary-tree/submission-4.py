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
            out.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                out[-1].append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return out