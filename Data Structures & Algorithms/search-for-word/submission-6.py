class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def helper(x,y, i):
            if i == len(word):
                return True

            if  min(x,y) <0 or x>= len(board) or y >= len(board[x]) or board[x][y] != word[i] or (x,y) in path:
                return False

            
            path.add((x,y))
            result = (helper(x+1, y, i+1) or
                helper(x, y+1, i+1) or
                helper(x-1, y, i+1) or
                helper(x, y-1, i+1))

            path.remove((x,y))
            return result


        for x in range(len(board)):
            for y in range(len(board[x])):
                if helper(x,y, 0):
                    return True

        return False