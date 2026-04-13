class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            first = heapq.heappop_max(heap)
            second = heapq.heappop_max(heap)

            if first == second:
                continue
            else:
                mi = min(first, second)
                ma = max(first,second)

                newStone = ma - mi
                heapq.heappush_max(heap, newStone)

        if len(heap) == 0:
            return 0
        return heap[0]