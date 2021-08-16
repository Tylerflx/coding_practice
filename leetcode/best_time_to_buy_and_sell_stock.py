"""
Success
Details 
Runtime: 972 ms, faster than 78.09% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.1 MB, less than 82.20% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_price = prices[0]
        total = 0
        for ind, num in enumerate (prices):
            if ind == len(prices):
                return 0
            if num < prev_price:
                prev_price = num
            if num - prev_price > total:
                total = num - prev_price
        return total