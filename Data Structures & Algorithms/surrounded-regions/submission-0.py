class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        direction = [(-1,0), (1,0), (0,1), (0,-1)]

        def capture(x,y):
            if board[x][y] == "O":
                board[x][y] = "T"
                for d in direction:
                    dx,dy = x+d[0], y+d[1]
                    if 0<= dx < rows and 0<= dy < cols and board[dx][dy] == "O":
                        capture(dx,dy)
        
        for i in range(rows): # left
            # print(i,0, board[i][0])
            capture(i, 0)
        
        for i in range(rows): # right
            # print(i,cols-1, board[i][cols-1])
            capture(i, cols-1)

        for i in range(cols): #top
            # print(0, i, board[0][i])
            capture(0, i)

        for i in range(cols): #bottom
            # print(rows-1, i, board[rows-1][i])
            capture(rows-1, i)

        print(board)

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "O":
                    board[x][y] = "X"
                if board[x][y] == "T":
                    board[x][y] = "O"
