from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (2 * n)
        k = 0
        for i in range(n):
            ans[k], ans[k+1] = nums[i], nums[i+n]
            k += 2
        return ans