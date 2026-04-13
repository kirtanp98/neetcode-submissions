import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            x,y = points[i][0], points[i][1]
            distance = math.sqrt(((x - 0)**2) + ((y - 0)**2))
            heapq.heappush(heap, [distance, [x,y]])

        return [points for _, points in heapq.nsmallest(k, heap)]