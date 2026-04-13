class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        square = [set() for _ in range(9)]

        print(board)

        for x in range(len(board)):
            for y in range(len(board[x])):
                num = board[x][y]

                if not num.isdigit():
                    continue
                rset = row[self.getRow(x,y)]
                cset = column[self.getColumn(x,y)]
                sset = square[self.getSquare(x,y)]


                if num in rset:
                    return False
                if num in cset:
                    return False
                if num in sset:
                    return False
                
                rset.add(num)
                cset.add(num)
                sset.add(num)
        
        return True

    def getColumn(self,x,y):
        return y
    def getRow(self,x,y):
        return x
    def getSquare(self,x,y):
        return ((x//3)*3 + y//3)

