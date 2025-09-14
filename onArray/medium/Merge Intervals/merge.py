from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[int]:
        intervals.copy().sort()
        ans = []
        if len(intervals) <= 1:
            return intervals
        newInterval = intervals[0]
        ans.append(newInterval)
        for interval in intervals:
            if interval[0] <= newInterval[1]:
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                newInterval = interval
                ans.append(newInterval)
        return ans
