class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def helper(i):
            if i >= len(s):
                result.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPal(i, j, s):
                    part.append(s[i: j+1])
                    helper(j+1)
                    part.pop()

        helper(0)

        return result
        


    def isPal(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            i +=1
            j -=1
        return True