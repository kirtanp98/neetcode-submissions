class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i,num in enumerate(nums):
            numNeeded = target - num
            if numNeeded in d:
                return [d[numNeeded], i]
            
            d[num] = i