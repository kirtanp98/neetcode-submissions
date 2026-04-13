class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]

        result = []
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        for key,v in d.items():
            bucket[v].append(key)

        for i in range(len(bucket)-1, -1, -1):
            if len(result) >= k:
                return result
            if len(bucket[i])> 0:
                for res in bucket[i]:
                    if len(result) <=k:
                        result.append(res)


        return result