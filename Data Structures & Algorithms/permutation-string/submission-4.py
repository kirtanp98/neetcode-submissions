class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)< len(s1):
            return False
        d = defaultdict(int)
        s1d = defaultdict(int)

        for s in s1:
            s1d[s] += 1
        
        for i in range(0, len(s1)):
            d[s2[i]] += 1

        l, r = 0, len(s1)

        while r < len(s2):
            print(d)
            if d == s1d:
                return True

            d[s2[r]] += 1
            d[s2[l]] -= 1
            print(d)
            if d[s2[l]] <= 0:
                d.pop(s2[l])
            r+=1
            l+=1


        return d == s1d