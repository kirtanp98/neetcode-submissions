class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        result = set()

        def helper(i, subset):
            if i == len(nums):
                result.add(tuple(subset))
                return
            
            subset.append(nums[i])
            helper(i+1, subset)
            subset.pop()
            helper(i+1, subset)

        nums.sort()
        helper(0, [])

        return [i for i in result]