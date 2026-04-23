class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def rec(i):
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(rec(i+1), rec(i+2))
            
            return memo[i]

        return min(rec(0), rec(1))