class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n,m = 1, max(piles)
        res = m
        while n <= m:
            k = (n+m) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                res = k
                m = k - 1
            else:
                n = k + 1
        
        return res