class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        direction = [(-1, 0), (1,0), (0,-1), (0,1)]
        visited = set()
        inf = 2147483647

        q = deque()


        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    q.append((x,y))
                    visited.add((x,y))

        distance = 0
        while q:
            for _ in range(len(q)):
                (x,y) = q.popleft()
                grid[x][y] = distance
                visited.add((x,y))
                for d in direction:
                    dx, dy = x+d[0], y +d[1]
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == inf and (dx,dy) not in visited:
                        q.append((dx,dy))
                        visited.add((dx,dy))

            distance += 1

        