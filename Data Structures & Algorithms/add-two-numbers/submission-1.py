# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = l1, l2
        r = ListNode()
        cr = r
        carry = 0
        while c1 and c2:
            cr.next = ListNode()
            cr = cr.next
            digit = c1.val + c2.val + carry
            if digit >= 10:
                carry = digit // 10
                digit = digit % 10
            else:
                carry = 0
            cr.val = digit
            c1 = c1.next
            c2 = c2.next
        rest = c1 if c1 else c2
        while rest:
            cr.next = ListNode()
            cr = cr.next
            digit = rest.val + carry
            if digit >= 10:
                carry = digit // 10
                digit = digit % 10
            else:
                carry = 0
            cr.val = digit
            rest = rest.next
        while carry > 0:
            cr.next = ListNode()
            cr = cr.next
            digit = carry
            if digit >= 10:
                carry = digit // 10
                digit = digit % 10
            else:
                carry = 0
            cr.val = digit

        return r.next


        