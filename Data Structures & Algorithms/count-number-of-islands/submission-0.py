class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
        rows, col = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(x,y):
            q = deque()
            grid[x][y] = "0"
            q.append((x,y))

            while q:
                x,y = q.popleft()

                for d in directions:
                    dx,dy = x+d[0], y+d[1]
                    if (dx,dy) and 0<= dx < rows and 0<= dy < col and grid[dx][dy] == "1":
                        q.append((dx,dy))
                        grid[dx][dy] = '0'

        for x in range(rows):
            for y in range(col):
                if grid[x][y] == "1":
                    bfs(x,y)
                    num_of_islands +=1


        return num_of_islands