class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = defaultdict(int)
        td = defaultdict(int)

        for x in s:
            sd[x]+=1
        for x in t:
            td[x]+=1

        for y in sd.keys():
            if sd[y] != td[y]:
                return False

        return True