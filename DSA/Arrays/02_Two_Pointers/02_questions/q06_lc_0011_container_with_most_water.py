"""LeetCode #11 - Container With Most Water."""
from typing import List


class BruteForce:
    def solve(self, height: List[int]) -> int:
        best = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                best = max(best, area)
        return best


class BetterSolution:
    def solve(self, height: List[int]) -> int:
        return OptimalSolution().solve(height)


class OptimalSolution:
    def solve(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            best = max(best, area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return best

