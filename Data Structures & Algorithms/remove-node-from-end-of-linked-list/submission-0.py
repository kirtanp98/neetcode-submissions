# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0

        p = head

        while p is not None:
            l += 1
            p = p.next
        
        removeNode = l-n
        print(removeNode)

        if removeNode == 0:
            head = head.next
            return head

        p2 = head
        current = 0
        while p2:
            if current == removeNode -1:
                p2.next = p2.next.next
            p2 = p2.next
            current +=1
        return head