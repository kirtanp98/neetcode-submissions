class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        columnSet = [set() for _ in range(9)]
        square = [set() for _ in range(9)]

        for x in range(len(board)):
            for y in range(len(board[x])):
                if not board[x][y].isdigit():
                    continue
                row, column, sq = self.rowIndexHelper(x,y), self.columnIndexHelper(x,y), self.squareIndexHelper(x,y)
                if board[x][y] in rowSet[row]:
                    print(board[x][y], "row")
                    return False
                if board[x][y] in columnSet[column]:
                    print(board[x][y], "col")
                    return False
                if board[x][y] in square[sq]:
                    print(board[x][y], "sq")
                    return False
                
                rowSet[row].add(board[x][y])
                columnSet[column].add(board[x][y])
                square[sq].add(board[x][y])
        return True

    def rowIndexHelper(self, x, y):
        return x;
    def columnIndexHelper(self, x, y):
        return y;
    def squareIndexHelper(self, x, y):
        return (x // 3) * 3 + (y // 3)