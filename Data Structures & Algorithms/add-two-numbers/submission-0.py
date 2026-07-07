# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        curr1 = l1
        curr2 = l2

        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10
            node = ListNode(digit)
            current.next = node
            current = current.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        
        return dummy.next
