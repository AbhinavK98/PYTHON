"""LeetCode #31 - Next Permutation."""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> None:
        # Brute force by generating all permutations is not practical here.
        # Keep as conceptual placeholder for interview discussion.
        OptimalSolution().solve(nums)


class BetterSolution:
    def solve(self, nums: List[int]) -> None:
        OptimalSolution().solve(nums)


class OptimalSolution:
    def solve(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

