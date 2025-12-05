from typing import List
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]

        heap = [-i for i in target]
        heapq.heapify(heap)
        total = sum(target)

        while -heap[0] > 1:
            maxx = -heapq.heappop(heap)
            rem = total - maxx

            if rem == 1:
                return True

            pre = maxx % rem

            if pre < 1 or pre == maxx:
                return False

            heapq.heappush(heap, -pre)
            total += pre - maxx
        return True


