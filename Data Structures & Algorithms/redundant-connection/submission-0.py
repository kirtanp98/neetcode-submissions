class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ver = defaultdict(list)
        result = []

        for (n,e) in edges:
            ver[n].append(e)
            ver[e].append(n)

        visted = set()
        cycle = set()
        self.cyclestart = -1

        def dfs(i, prev):

            if i in visted:
                self.cyclestart = i
                return True

            visted.add(i)

            for e in ver[i]:
                if e == prev:
                    continue
                if dfs(e, i):
                    if self.cyclestart != -1:
                        cycle.add(i)
                    if i == self.cyclestart:
                        self.cyclestart = -1
                    return True
            return False
        
        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]

        return []