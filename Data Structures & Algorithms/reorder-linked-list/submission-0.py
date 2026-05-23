# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        curr, next = head, head.next
        tcurr, tnext = prev, prev.next
        while next and tnext:
            print(curr.val, tcurr.val)
            curr.next = tcurr
            tcurr.next = next
            tcurr, tnext = tnext, tnext.next
            curr, next = next, next.next

