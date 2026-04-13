class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longestSequence = 0

        for n in s:
            if n-1 not in s:
                # start of sequence
                l = 0
                while n in s:
                    n += 1
                    l += 1
                longestSequence = max(longestSequence, l)

        return longestSequence