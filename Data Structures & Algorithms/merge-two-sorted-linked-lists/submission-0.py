# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        p1 = list1
        p2 = list2

        if p1.val >= p2.val:
            head = p2
            p2 = p2.next
        else:
            head = p1
            p1 = p1.next

        p3 = head

        while p1 is not None and p2 is not None:
            print(head)
            if p1.val >= p2.val:
                p3.next = p2
                p2 = p2.next
            else:
                p3.next = p1
                p1 = p1.next
            
            p3 = p3.next

        if p1 is None:
            p3.next = p2
        else:
            p3.next = p1

        return head