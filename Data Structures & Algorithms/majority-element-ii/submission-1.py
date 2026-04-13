class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        result = []

        for x in nums:
            d[x] +=1

        for y in d:
            if d[y] > len(nums)/3:
                result.append(y)


        return result