class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        result = []

        for x in nums:
            d[x] +=1

            if len(d) < 3:
                continue
            new_d = defaultdict(int)
            for i,x in d.items():
                if d[i] > 1:
                    new_d[i] = x -1
            d = new_d

        for x in d:
            if nums.count(x) > len(nums) //3:
                result.append(x)
        return result