class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0 or len(s) == 1:
            return len(s)

        l = 0
        se = set()

        result = 0

        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l+= 1
            se.add(s[r])
            result = max(result, r-l+1)
        
        return result
