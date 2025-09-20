class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        maxC = 1
        ans = 1
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                maxC += 1
            else:
                maxC = 1
            ans = max(ans, maxC)
            i += 1
        return ans