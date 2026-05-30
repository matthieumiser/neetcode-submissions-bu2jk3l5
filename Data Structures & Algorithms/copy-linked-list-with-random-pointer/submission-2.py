"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new_head = Node(0)
        hashmap = {}
        curr = head
        new_curr = new_head

        while curr:
            new_curr.val = curr.val
            if curr.next:
                new_curr.next = Node(0)
            hashmap[curr] = new_curr

            # advance
            curr = curr.next
            new_curr = new_curr.next
        
        curr = head
        new_curr = new_head

        while curr:
            if curr.random:
                new_curr.random = hashmap[curr.random]

            # advance
            curr = curr.next
            new_curr = new_curr.next
        
        return new_head
