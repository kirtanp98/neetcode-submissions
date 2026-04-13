class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        pivot = l
        
        left = self.binary_search(nums[0:pivot], target)
        right = self.binary_search(nums[pivot:len(nums)], target)

        if left > -1:
            return left
        elif right>-1:
            return pivot+ right
        return -1

    def binary_search(self, nums, target) -> int:
        l, r = 0, len(nums) - 1

        while l <=r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid +1
            else:
                r = mid -1
        return -1