class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while l < r:
            s1 = s[l]
            s2 = s[r]
            s[l] = s2
            s[r] = s1

            l += 1
            r -= 1