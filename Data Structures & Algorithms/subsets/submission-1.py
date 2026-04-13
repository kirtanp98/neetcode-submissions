class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(i, subset):
            if i >= len(nums):
                result.append(subset.copy())
                return
        
            subset.append(nums[i])
            helper(i +1, subset.copy())

            subset.pop()
            helper(i +1, subset.copy())
        helper(0, [])
        return result
