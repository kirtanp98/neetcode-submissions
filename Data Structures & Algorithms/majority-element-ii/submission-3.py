class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)

        for x in nums:
            d[x] +=1
            if len(d) < 3:
                continue
            
            new_d = defaultdict(int)

            for y in d:
                if d[y] > 1:
                    new_d[y] = d[y] -1

            d = new_d

        result = []
        for x in d:
            if nums.count(x) > len(nums)//3:
                result.append(x)
        return result