# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        cur = result

        p = l1
        p2 = l2

        carry = 0
        newDumb = None
        while carry or p or p2:
            v1 = p.val if p else 0
            v2 = p2.val if p2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            total = total % 10
            

            newNode = ListNode(total)
            cur.next = newNode

            cur = cur.next
            if p:
                p = p.next
            if p2:
                p2 = p2.next



        return result.next