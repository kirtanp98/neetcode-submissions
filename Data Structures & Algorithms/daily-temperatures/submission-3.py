class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, x in enumerate(temperatures):
            while stack and x > temperatures[stack[-1]]:
                stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append(i)
        return result