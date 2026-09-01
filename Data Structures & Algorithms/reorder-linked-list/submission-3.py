# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       # first find the middle
       # 0 1 2 3 4 5 6        
       #       m

       # reverse the second half
       # 0 1 2 3    6 5 4

       # merge the two lists
       # 0 6 1 5 2 4 3             


       slow = head
       fast = head

       while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

       curr = slow.next
       slow.next = None
       prev = None
       while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
        
       first = head
       second = prev

       while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

       




                 