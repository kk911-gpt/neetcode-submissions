from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)

        # Python has a min heap, so use negative frequencies
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)

        time = 0

        while maxHeap:
            temp = []

            # We can process at most n + 1 tasks
            for _ in range(n + 1):
                
                if maxHeap:
                    freq = heapq.heappop(maxHeap)
                    freq += 1  # One occurrence completed

                    if freq != 0:
                        temp.append(freq)

                time += 1

                # If no tasks are left, don't need to fill
                # the remaining slots with idle
                if not maxHeap and not temp:
                    break

            # Put unfinished tasks back into heap
            for freq in temp:
                heapq.heappush(maxHeap, freq)

        return time