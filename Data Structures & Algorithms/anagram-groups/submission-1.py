from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def keyGen(string):
            def getPostion(c):
                return ord(c) - ord('a')
            
            alphaString = [0]*26

            for char in string:
                alphaString[getPostion(char)]+=1
            
            return alphaString
            
        resultMap = defaultdict(list)

        for s in strs:
            key = keyGen(s)
            resultMap[tuple(key)].append(s)

        return list(resultMap.values())