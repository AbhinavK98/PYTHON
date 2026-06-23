"""LeetCode #121 - Best Time to Buy and Sell Stock."""
from typing import List


class BruteForce:
    def solve(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                best = max(best, prices[j] - prices[i])
        return best


class BetterSolution:
    def solve(self, prices: List[int]) -> int:
        return OptimalSolution().solve(prices)


class OptimalSolution:
    def solve(self, prices: List[int]) -> int:
        min_price = float('inf')
        best_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            best_profit = max(best_profit, price - min_price)
        return best_profit

