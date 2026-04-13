from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1

        arrayFreq = [(v,x) for x,v in count.items()]

        heapq.heapify_max(arrayFreq)
        result = []
        n = 0

        while n<k:
            result.append(heapq.heappop_max(arrayFreq)[1])
            n+=1

        return result;
