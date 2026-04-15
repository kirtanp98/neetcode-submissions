class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def helper(i, subset):
            if len(subset) == len(digits):
                result.append(subset)
                return
            for c in phone[digits[i]]:
                helper(i+1, subset+c)



        if digits:
            helper(0, "")
        

        return result