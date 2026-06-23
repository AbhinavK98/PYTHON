"""LeetCode #169 - Majority Element."""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> int:
        for value in nums:
            if nums.count(value) > len(nums) // 2:
                return value
        return -1


class BetterSolution:
    def solve(self, nums: List[int]) -> int:
        freq = {}
        for value in nums:
            freq[value] = freq.get(value, 0) + 1
            if freq[value] > len(nums) // 2:
                return value
        return -1


class OptimalSolution:
    def solve(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for value in nums:
            if count == 0:
                candidate = value
            count += 1 if value == candidate else -1
        return candidate

