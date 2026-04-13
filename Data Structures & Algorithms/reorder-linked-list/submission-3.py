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

        print()

        while p and p2:

            print(p.val, p2.val)
            temp = p.next
            p.next = ListNode(p2.val, temp)
            p2 = p2.next
            p = p.next.next

            
