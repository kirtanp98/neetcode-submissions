class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size_of_island = 0
        row, col = len(grid), len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def helper(x,y):
            q = deque()
            grid[x][y] = 0
            q.append((x,y))

            size = 0
            while q:
                (x,y) = q.popleft()
                size += 1

                for d in directions:
                    dx,dy = x+d[0], y+d[1]
                    print(dx,dy)

                    if (dx,dy) and 0<= dx < row and 0<= dy < col and grid[dx][dy] == 1:
                        q.append((dx,dy))
                        grid[dx][dy] = 0

            return size

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    size = helper(x,y)
                    max_size_of_island = max(size, max_size_of_island)

        return max_size_of_island