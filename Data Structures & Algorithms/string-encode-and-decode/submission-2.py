class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for s in strs:
            encodedString += str(len(s))+ "#" + s

        print(encodedString)
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedArray = []

        currentLen = ""
        i = 0
        while i < len(s):
            if s[i] == "#":
            # add string to array
                lenOfWord = int(currentLen)
                currentLen = ""
                word = s[i+1: i+1+ lenOfWord]
                decodedArray.append(word)
                i += lenOfWord + 1

            elif s[i].isdigit():
                currentLen += s[i]
                i += 1

        return decodedArray