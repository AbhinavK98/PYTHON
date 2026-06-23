"""LeetCode #303 - Range Sum Query Immutable."""
from typing import List


class BruteForceNumArray:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.nums[left : right + 1])


class BetterNumArray:
    def __init__(self, nums: List[int]) -> None:
        self.prefix = [0]
        for value in nums:
            self.prefix.append(self.prefix[-1] + value)

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


class OptimalNumArray(BetterNumArray):
    pass

