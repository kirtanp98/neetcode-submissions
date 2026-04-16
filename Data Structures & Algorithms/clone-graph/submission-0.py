"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        oldToCopy = defaultdict(lambda: Node())

        oldToCopy[None] = None


        oldToCopy[node] = Node(node.val)
        q = deque()
        q.append(node)

        while q:
            current = q.popleft()
            for n in current.neighbors:
                if n not in oldToCopy:
                    oldToCopy[n] = Node(n.val)
                    q.append(n)
                oldToCopy[current].neighbors.append(oldToCopy[n])              

        return oldToCopy[node]