class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def helper(i):
            if i >= len(s):
                result.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(i,j, s):
                    part.append(s[i : j+1])
                    helper(j+1)
                    part.pop()

        helper(0)

        print(result)
        return result
        
    def isPalindrome(self, p1, p2, s):
        while p1 < p2:
            
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1

        return True