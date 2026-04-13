class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1

        l = 0
        r = len(nums)-1

        if len(nums) == 1 and nums[0] == target:
            return 0

        while l <= r:
            mid = l + ((r-l) // 2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1


        return result