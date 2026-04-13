class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        if len(s) != len(t):
            return False
        
        for n in s:
            if n in dic1:
                dic1[n] += 1
            else:
                dic1[n]=1
        for n in t:
            if n in dic2:
                dic2[n] += 1
            else:
                dic2[n]=1

        if (len(dic1) != len(dic2)):
            return False
        
        for x in dic1:
            if (x not in dic2):
                return False
            if dic1[x] != dic2[x]:
                return False

        return True