class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [c for c in count.values()]
        heapq.heapify_max(max_heap)
        print(max_heap)

        time = 0

        q = deque()

        while max_heap or q:
            time +=1

            if not max_heap and q:
                time = q[0][1]
            else:
                c = heapq.heappop_max(max_heap) -1
                if c:
                    q.append([c, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(max_heap, q.popleft()[0])

        return time