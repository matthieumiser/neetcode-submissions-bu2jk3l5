from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = Node(val=node.val)
        q = deque([node])
        cq = deque([clone])
        visited = set()
        mapping = {}
        mapping[node] = clone
        while q:
            curr = q.popleft()
            clonecurr = cq.popleft()
            if curr and curr not in visited:
                for n in curr.neighbors:
                    if n not in mapping: mapping[n] = Node(n.val)
                    clonecurr.neighbors.append(mapping[n])
                    q.append(n)
                    cq.append(mapping[n])
            visited.add(curr)

        return clone