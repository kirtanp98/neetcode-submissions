class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0

        result = 0

        while r < len(prices):
            price = prices[r] - prices[l]
            result = max(price, result)

            if prices[r] <= prices[l]:
                l = r
            r += 1

        return result