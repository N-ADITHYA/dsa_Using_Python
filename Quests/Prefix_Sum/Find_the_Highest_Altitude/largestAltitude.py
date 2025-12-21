from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        newArr = [0] * (len(gain) + 1)
        maxA = 0
        for i in range(1, len(gain) + 1):
            newArr[i] = newArr[i - 1] + gain[i - 1]
            if newArr[i] > maxA:
                maxA = newArr[i]
        return maxA