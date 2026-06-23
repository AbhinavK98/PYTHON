"""LeetCode #283 - Move Zeroes."""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> None:
        non_zero = [x for x in nums if x != 0]
        zero_count = len(nums) - len(non_zero)
        nums[:] = non_zero + [0] * zero_count


class BetterSolution:
    def solve(self, nums: List[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1


class OptimalSolution(BetterSolution):
    pass

