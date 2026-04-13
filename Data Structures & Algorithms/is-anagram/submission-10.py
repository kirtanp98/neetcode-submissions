class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d, dd = {}, {}

        for i in range(len(s)):
            d[s[i]] = 1 + d.get(s[i], 0)
            dd[t[i]] = 1 + dd.get(t[i], 0)

        return d == dd