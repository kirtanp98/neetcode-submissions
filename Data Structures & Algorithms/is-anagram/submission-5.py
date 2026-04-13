class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dicS, dicT = {}, {}

        for n in range(len(s)):
            dicS[s[n]] = 1 + dicS.get(s[n], 0)
            dicT[t[n]] = 1 + dicT.get(t[n], 0)

        for c in dicS:
            if dicS[c] != dicT.get(c, ""):
                return False
        return True