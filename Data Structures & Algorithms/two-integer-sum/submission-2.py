class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}

        for i, n in enumerate(nums):
            if n in mem:
                return [mem[n], i]
            meow = target - n
            mem[meow] = i
        
        return []