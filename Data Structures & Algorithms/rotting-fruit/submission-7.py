class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        direction = [(-1,0), (1,0), (0, 1), (0, -1)]
        minutes = 0
        fresh_fruit = set()
        q = deque()

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    q.append((x,y))
                if grid[x][y] == 1:
                    fresh_fruit.add((x,y))


        if len(q) == 0 and len(fresh_fruit) ==  0:
            return 0
        elif len(q) == 0 and len(fresh_fruit) >  0:
            return -1

        


        while len(fresh_fruit) > 0 and q:
            for i in range(len(q)):
                (x,y) = q.popleft()
                for d in direction:
                    dx, dy = x+d[0], y+d[1]
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1 and (dx,dy) in fresh_fruit:
                        q.append((dx,dy))
                        fresh_fruit.remove((dx, dy))
                        grid[dx][dy] = 2

            minutes += 1
            
        
        if len(fresh_fruit) > 0:
            return -1

        return minutes 