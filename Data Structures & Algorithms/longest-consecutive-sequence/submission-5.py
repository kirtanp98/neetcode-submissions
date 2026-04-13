class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxCons = 0

        for nums in numSet:
            if nums + 1 in numSet:
                length = 1
                while (nums + length) in numSet:
                    length += 1
                maxCons = max(maxCons, length)
            else:
                maxCons = max(maxCons, 1)

        return maxCons