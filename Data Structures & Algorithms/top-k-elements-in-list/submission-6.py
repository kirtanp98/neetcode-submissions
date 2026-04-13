class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1

 
        # freq[i] holds all numbers that appear i times
        freq = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)

        res = []
        for c in range(len(freq) - 1, 0, -1):  # from highest frequency down
            for num in freq[c]:
                res.append(num)
                if len(res) == k:
                    return res