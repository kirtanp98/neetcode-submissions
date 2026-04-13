class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []

        p = 0
        size = ""
        while p < len(s):
            if s[p] == "#":
                intSize = int(size)
                result.append(s[p+1: p+intSize+1])
                p += intSize
                size = ""
            elif s[p].isdigit():
                size += s[p]
            p +=1
        return result
