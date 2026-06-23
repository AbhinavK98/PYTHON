"""
Question: Two Sum
LeetCode: #1
Difficulty: Easy
Pattern: HashMap Complement

Problem Statement:
Given an integer array and a target, return indices of two numbers such that
those two numbers add up to target.

Why this pattern:
For each number x, we need (target - x). A hash map lets us answer
"Have we seen this needed value?" in O(1) average time.
"""

from typing import Dict, List


class BruteForce:
    """Check every pair using nested loops."""

    def solve(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


class BetterSolution:
    """Sort copy + two pointers (keeps original indices separately)."""

    def solve(self, nums: List[int], target: int) -> List[int]:
        indexed = [(value, index) for index, value in enumerate(nums)]
        indexed.sort(key=lambda item: item[0])

        left, right = 0, len(indexed) - 1
        while left < right:
            current_sum = indexed[left][0] + indexed[right][0]
            if current_sum == target:
                return [indexed[left][1], indexed[right][1]]
            if current_sum < target:
                left += 1
            else:
                right -= 1
        return []


class OptimalSolution:
    """One-pass hash map complement lookup."""

    def solve(self, nums: List[int], target: int) -> List[int]:
        seen: Dict[int, int] = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], index]
            seen[value] = index

        return []


if __name__ == '__main__':
    print(OptimalSolution().solve([2, 7, 11, 15], 9))

