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
                if first > second:
                    newStone = first - second
                    heapq.heappush_max(heap, newStone)
                else:
                    newStone = second - first
                    heapq.heappush_max(heap, newStone)


        if len(heap) == 0:
            return 0
        return heap[0]