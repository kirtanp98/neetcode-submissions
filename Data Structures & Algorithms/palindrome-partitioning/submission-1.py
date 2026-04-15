class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def helper(i):
            if i >= len(s):
                result.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    part.append(s[i : j+1])
                    helper(j+1)
                    part.pop()

        helper(0)

        print(result)
        return result
        
    def isPalindrome(self, s:str):
        p1 = 0
        p2 = len(s)-1

        while p1 < p2:
            while p1 < p2 and not s[p1].isalnum():
                p1 += 1
            while p1 < p2 and not s[p2].isalnum():
                p2 -= 1
            
            print(s[p1].lower(), s[p2].lower())
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1

        return True