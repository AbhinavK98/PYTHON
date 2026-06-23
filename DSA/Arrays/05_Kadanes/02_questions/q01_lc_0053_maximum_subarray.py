"""LeetCode #53 - Maximum Subarray."""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> int:
        best = nums[0]
        for i in range(len(nums)):
            current = 0
            for j in range(i, len(nums)):
                current += nums[j]
                best = max(best, current)
        return best


class BetterSolution:
    def solve(self, nums: List[int]) -> int:
        return OptimalSolution().solve(nums)


class OptimalSolution:
    def solve(self, nums: List[int]) -> int:
        # Kadane's: max subarray ending here.
        best_ending_here = nums[0]
        best_so_far = nums[0]

        for i in range(1, len(nums)):
            best_ending_here = max(nums[i], best_ending_here + nums[i])
            best_so_far = max(best_so_far, best_ending_here)

        return best_so_far

