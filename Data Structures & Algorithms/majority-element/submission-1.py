class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        result = 0
        maxNum = 0

        for x in nums:
            d[x] += 1
            if d[x] >= maxNum:
                maxNum = d[x]
                result = x

        return result
