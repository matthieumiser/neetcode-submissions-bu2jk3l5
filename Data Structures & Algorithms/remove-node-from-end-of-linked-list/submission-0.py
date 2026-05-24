# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        sz = 0
        while tail:
            tail = tail.next
            sz += 1
        if sz == n:
            return head.next
        rm_idx = sz - n

        curr = head
        i = 1
        while i < rm_idx:
            curr = curr.next
            i += 1
        
        rm = curr.next
        curr.next = rm.next
        return head