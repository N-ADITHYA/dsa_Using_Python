from typing import List


class Solution:
    def minMax(self, nums: List[int], m: int) -> int:

        if len(nums) == 0 or m == 0:
            return 0

        nums.sort()
        if len(nums) < m:
            return -1
        minD = float('inf')
        for i in range(len(nums) - m + 1):
            diff = nums[i + m - 1] - nums[i]
            if diff < minD:
                minD = diff
        return minD


