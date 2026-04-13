class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def helper(string: str):
            key = [0]*27
            for s in string:
                index = ord(s) - 96
                key[index] += 1

            
            return tuple(key)

        resultD = defaultdict(list)

        for word in strs:
            k = helper(word)

            resultD[k].append(word)
                
        return list(resultD.values())