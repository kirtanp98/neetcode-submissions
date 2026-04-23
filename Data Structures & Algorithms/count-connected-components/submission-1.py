class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        result = 0
        ver = defaultdict(list)

        for (node, e) in edges:
            ver[node].append(e)
            ver[e].append(node)

        print(ver)

        visted = set()


        def bfs(i):
            q = deque([i])
            print(i)

            while q:
                visiting = q.popleft()
                visted.add(visiting)
                for edge in ver[visiting]:
                    if edge not in visted:
                        q.append(edge)
            

        
        for i in range(n):
            if i not in visted:
                bfs(i)
                result +=1


        


        return result