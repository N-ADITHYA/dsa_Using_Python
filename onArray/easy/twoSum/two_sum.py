from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums = nums.copy()
        seen = {}
        for ind, num in enumerate(nums):
            complement = target - nums[ind]
            if complement in seen:
                return [seen[complement], ind]
            seen[num] = ind
        return []

