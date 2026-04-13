class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1

        while l <= r:
            mid = l + ((r-l) // 2)
            cm, cn = self.indexHelper(m,n, mid)

            if matrix[cm][cn] == target:
                return True
            elif target > matrix[cm][cn]:
                l = mid + 1
            else:
                r = mid - 1

        return False
    
    def indexHelper(self, m: int, n: int, index: int) -> [int, int]:
        row = index // n
        column = index % n

        return [row, column]