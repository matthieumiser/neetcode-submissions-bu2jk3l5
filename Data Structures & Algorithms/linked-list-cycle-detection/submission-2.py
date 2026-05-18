# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            fast = head.next.next
        else:
            return False
        slow = head
        while fast:
            if fast == slow:
                return True
            if fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
        
        return False