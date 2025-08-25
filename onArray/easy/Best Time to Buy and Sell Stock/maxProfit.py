from typing import List

# Main logic to run maxProfit
# Run driver code to view output

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        j = 0
        for i in range(j+1, len(prices)):
            if prices[i] > prices[j]:
                ans = max(prices[i] - prices[j], ans)
            else:
                j = i
        return ans

