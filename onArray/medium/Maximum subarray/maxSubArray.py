from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> List[int]:
        nums = nums.copy()
        curr_sum = 0
        ans = float('-inf')
        for i in range(len(nums)):
            curr_sum += nums[i]
            ans = max(ans, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return ans
