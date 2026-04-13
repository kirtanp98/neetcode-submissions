class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        j = 0

        while j < len(nums):
            if j > 0 and nums[j] == nums[j - 1]:
                j += 1
                continue

            l, r = j + 1, len(nums) - 1

            while l < r:
                t = nums[j] + nums[l] + nums[r]

                if t == 0:
                    result.append([nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif t < 0:
                    l += 1
                else:
                    r -= 1

            j += 1

        return result