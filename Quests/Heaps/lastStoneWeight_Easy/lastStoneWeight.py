from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Bro we have to use heapq in here
        #okk we ll import heap now
        import heapq


        # convert every element into negative value
        # coz python doesn't have native max heap function, so negating it will help in mimiking max heap
        stones = [-s for s in stones]

        # then using python's inbuilt heapq library we did this
        heapq.heapify(stones)

        while len(stones) > 1:
            f = heapq.heappop(stones)
            s = heapq.heappop(stones)
            if s > f:
                heapq.heappush(stones, f - s)
        stones.append(0)
        return abs(stones[0])



