class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            helper(i, curr, total + nums[i])
            curr.pop()
            helper(i +1, curr, total)


        helper(0, [], 0)
        return result
