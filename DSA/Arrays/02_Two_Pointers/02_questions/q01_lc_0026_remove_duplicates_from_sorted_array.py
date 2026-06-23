"""LeetCode #26 - Remove Duplicates from Sorted Array."""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        for i, value in enumerate(unique):
            nums[i] = value
        return len(unique)


class BetterSolution:
    def solve(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
        return write


class OptimalSolution(BetterSolution):
    pass

