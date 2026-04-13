class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsR = []
        dic = {}

        for x in range(len(nums)):
            diff = target - nums[x]
            
            if diff in dic:
                return [dic[diff], x]
            else:
                dic[nums[x]] = x
        return []       