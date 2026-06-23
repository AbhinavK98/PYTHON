"""LeetCode #643 - Maximum Average Subarray I."""
from typing import List


class BruteForce:
    def solve(self, nums: List[int], k: int) -> float:
        best = float('-inf')
        for i in range(len(nums) - k + 1):
            best = max(best, sum(nums[i : i + k]))
        return best / k


class BetterSolution:
    def solve(self, nums: List[int], k: int) -> float:
        return OptimalSolution().solve(nums, k)


class OptimalSolution:
    def solve(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        best_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right - k]
            best_sum = max(best_sum, window_sum)

        return best_sum / k

