class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pset, aset = set(), set()

        def dfs(x,y, se, prevH):
            if (x,y) in se or x <0 or y <0 or x >= rows or y >= cols or heights[x][y] < prevH:
                return
            se.add((x,y))

            dfs(x+1,y, se, heights[x][y])
            dfs(x-1,y, se, heights[x][y])
            dfs(x,y+1, se, heights[x][y])
            dfs(x,y-1, se, heights[x][y])
        
        # top and bottom
        for y in range(cols):
            dfs(0, y, pset, heights[0][y])
            dfs(rows-1, y, aset, heights[rows-1][y])

        for x in range(rows):
            dfs(x, 0, pset, heights[x][0])
            dfs(x, cols-1, aset, heights[x][cols-1])
        

        result = []

        for x in range(rows):
            for y in range(cols):
                if (x,y) in pset and (x,y) in aset:
                    result.append([x,y])

        return result