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
        
        curr = head
        while curr:
            curr.next, curr = Node(curr.val, next=curr.next), curr.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

            even_head = even = head

        even_head = even = head
        odd_head = odd = head.next
        while odd and odd.next:
            even.next = odd.next
            even = even.next
            odd.next = even.next
            odd = odd.next
        even.next = None
        return odd_head