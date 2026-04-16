class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        direction = [(-1, 0), (1,0), (0,-1), (0, 1)]
        rows, columns = len(grid), len(grid[0])

        def bfs(x,y):
            q = deque()
            grid[x][y] = 0

            q.append((x,y))

            size = 0

            while q:
                (cx,cy) = q.popleft()
                size +=1

                for d in direction:
                    dx, dy = cx + d[0], cy+ d[1]

                    if 0<= dx <rows and 0<= dy <columns and grid[dx][dy] == 1:
                        q.append((dx,dy))
                        grid[dx][dy] = 0
            return size


        for x in range(rows):
            for y in range(columns):
                if grid[x][y]== 1:
                    max_island = max(max_island, bfs(x,y))

        return max_island