class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_value = 0
        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                max_value = max(max_value, prices[right] - prices[left])
            elif prices[left >= prices[right]]:
                left = right

        return max_value