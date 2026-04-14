class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap_max = [c for c in count.values()]
        heapq.heapify_max(heap_max)

        q = deque()
        time = 0
        
        while heap_max or q:
            time +=1

            if not heap_max:
                time = q[0][1]
            else:
                c = heapq.heappop_max(heap_max) - 1
                if c:
                    q.append([c, time+n])
                
            if q and time == q[0][1]:
                heapq.heappush_max(heap_max, q.popleft()[0])


        return time