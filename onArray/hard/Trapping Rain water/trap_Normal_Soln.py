from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * (len(height))
        maxR = [0] * (len(height))
        maxx = 0
        ans = []
        for i in range(1,len(height)):
            maxL[i] = max(maxx, height[i-1])
            maxx = max(maxx, height[i-1])

        maxx = 0
        for j in range(len(height)-2, -1, -1):
            maxR[j] = max(maxx, height[j+1])
            maxx = max(maxx, height[j + 1])

        for k in range(len(maxL)):
            ans.append((min(maxL[k], maxR[k]) - height[k]) if (min(maxL[k], maxR[k]) - height[k]) > 0 else 0)
        return sum(ans)
