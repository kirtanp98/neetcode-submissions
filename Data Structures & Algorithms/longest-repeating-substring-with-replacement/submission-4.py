class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        d = {}

        result = 0
        currentK = k
        maxf = 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            maxf = max(maxf, d[s[r]])
            while (r-l+1) - maxf > k:
                d[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        
        return result
    