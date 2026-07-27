class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                output = max(output, prices[j] - prices[i])

        return output