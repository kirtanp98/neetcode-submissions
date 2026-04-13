class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        result = set()

        for x in nums:
            d[x] +=1
            if d[x] > len(nums)/3:
                result.add(x)


        return list(result)