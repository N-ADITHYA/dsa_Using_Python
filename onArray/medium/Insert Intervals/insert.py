from typing import List

class Solution:
    def insert(self, interval: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr = []
        i = 0
        while i < len(interval) and interval[i][1] < newInterval[0]:
            arr.append(interval[i])
            i += 1

        while i < len(interval) and interval[i][0] <= newInterval[1]:
            newInterval[0] = min(interval[i][0], newInterval[0])
            newInterval[1] = max(interval[i][1], newInterval[1])
            i += 1
        arr.append(newInterval)

        while i < len(interval):
            arr.append(interval[i])
            i += 1

        return arr