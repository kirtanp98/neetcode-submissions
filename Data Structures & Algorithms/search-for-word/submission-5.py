class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.result = False

        def helper(x,y, i, se):
            if i == len(word):
                self.result = True
                return

            if (x, y) in se:
                return

            if i < len(word) and board[x][y] == word[i]:
                se.add((x,y))
                i += 1
            else:
                return

            if i == len(word):
                self.result = True
                return
            
            if x+1 < len(board):
                helper(x+1, y, i, se.copy())
            if y+1 < len(board[x]):
                helper(x, y+1, i, se.copy())
            if x-1 >= 0:
                helper(x-1, y, i, se.copy())
            if y-1 >= 0:
                helper(x, y-1, i, se.copy())
            return


        for x in range(len(board)):
            for y in range(len(board[x])):
                helper(x,y, 0, set())

        return self.result