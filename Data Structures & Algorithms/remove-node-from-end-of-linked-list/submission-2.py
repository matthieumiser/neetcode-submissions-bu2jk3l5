# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast, slow = head, dummy
        for _ in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next

        rm = slow.next
        slow.next = rm.next
        return dummy.next

