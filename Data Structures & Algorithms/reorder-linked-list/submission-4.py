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

        # reverse
        prev = None
        rhead = slow.next
        slow.next = None

        while rhead:
            temp = rhead.next
            rhead.next = prev
            prev = rhead
            rhead = temp
        
        p = head
        p2 = prev


        p1 = head
        p2 = prev

        while p2:
            t1 = p1.next
            t2 = p2.next

            p1.next = p2
            p2.next = t1

            p1 = t1
            p2 = t2

            
