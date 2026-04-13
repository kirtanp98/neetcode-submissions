# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        p = head

        while p is not None:
            p2 = p.next
            p.next = prev
            prev = p
            p = p2
        return prev
