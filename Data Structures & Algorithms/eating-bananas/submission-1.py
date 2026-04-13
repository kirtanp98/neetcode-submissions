class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n,m =1, max(piles)
        print(n,m)
        
        res = m
        while n <= m:
            mid = (n+m) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)

            if hours <= h:
                res = mid
                m = mid-1
            else:
                n = mid +1


        return res