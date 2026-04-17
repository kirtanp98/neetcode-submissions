class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False

        dic = defaultdict(lambda: [])

        for u, v in edges:
            dic[u].append(v)
            dic[v].append(u)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in dic[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        print(len(visit))
        return dfs(0, -1) and len(visit) == n