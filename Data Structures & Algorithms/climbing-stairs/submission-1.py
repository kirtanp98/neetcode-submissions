class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def rec(i):
            if i == n:
                return 1
            if i > n:
                return 0
            # if i >= n:
            #     return i == n

            if i in memo:
                return memo[i]

            memo[i] = rec(i+1) + rec(i+2)
            return memo[i]
        
        return rec(0)