class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []


        def helper(op, close, subset):
            if op == n and close == n:
                result.append(subset)
                return

            if op <= n:
                subset += "("
                helper(op +1, close, subset)
                subset = subset[:-1]
            if close <= n and op > close:
                subset += ")"
                helper(op, close+1, subset)
                subset = subset[:-1]

        helper(0,0, "")

        return result