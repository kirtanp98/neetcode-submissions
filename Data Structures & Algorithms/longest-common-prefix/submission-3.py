class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i in range(0, len(strs[0])+1):
            currentSub = strs[0][0:i]
            stop = False
            for s in range(1, len(strs)):
                if not (i <= len(strs[s]) and currentSub == strs[s][0:i]):
                    stop = True
                    break
            if stop:
                break
            else:
                result = currentSub


        return result