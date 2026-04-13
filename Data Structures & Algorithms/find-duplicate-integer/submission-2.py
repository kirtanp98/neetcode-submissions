class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        intersecting_slow = 0
        
        while slow != intersecting_slow:
            slow = nums[slow]
            intersecting_slow = nums[intersecting_slow]

        return slow