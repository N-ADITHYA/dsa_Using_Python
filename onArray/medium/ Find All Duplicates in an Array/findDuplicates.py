from typing import List

class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        ans = []
        for i in arr:
            if arr[abs(i) - 1] < 0:
                ans.append(abs(i))
            arr[abs(i) - 1] *= -1
        return ans