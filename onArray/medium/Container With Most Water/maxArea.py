from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heights = heights.copy()
        i, j = 0, len(heights) - 1
        ans = 0
        while i < j:
            h = min(heights[i], heights[j]) * (j - i)
            ans = max(ans, h)
            if heights[i] > heights[j]:
                j -= 1
            elif heights[j] >= heights[i]:
                i += 1
        return ans