"""LeetCode #27 - Remove Element."""
from typing import List


class BruteForce:
    def solve(self, nums: List[int], val: int) -> int:
        kept = [x for x in nums if x != val]
        nums[: len(kept)] = kept
        return len(kept)


class BetterSolution:
    def solve(self, nums: List[int], val: int) -> int:
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write


class OptimalSolution(BetterSolution):
    pass

