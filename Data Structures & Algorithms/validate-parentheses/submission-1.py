class Solution:
    def isValid(self, s: str) -> bool:
        end = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        if len(s) % 2 == 1:
            return False

        stack = []

        for p in s:
            if p not in end:
                stack.append(p)
            elif p in end and len(stack)> 0 and end[p] == stack[-1]:
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True

        return False

