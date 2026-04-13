"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        random = {}
        valToNew = {}
        newHead = Node(head.val,None, None)
        # random[newHead] = head.random

        p = head
        p2 = newHead
        
        while p:
            random[p2] = p.random
            valToNew[p] = p2
            p = p.next
            if p:
                p2.next = Node(p.val, None, None)
                p2 = p2.next
            else:
                p2.next = None

        print(random)
        print()
        print(valToNew)
        newp = newHead
        while newp:
            r = random[newp]
            if r:
                newp.random = valToNew[r]
            newp = newp.next


        return newHead