class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        dd = {}

        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        for c in t:
            if c in dd:
                dd[c] += 1
            else:
                dd[c] = 1
        
        if len(d) != len(dd):
            return False

        for v in d.keys():
            if v not in dd or d[v] != dd[v]:
                return False

        return True