"""
Question: Contains Duplicate
LeetCode: #217
Difficulty: Easy
Pattern: HashMap/HashSet lookup
"""

from typing import List, Set


class BruteForce:
    def solve(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


class BetterSolution:
    def solve(self, nums: List[int]) -> bool:
        # Sorting makes equal values adjacent.
        sorted_nums = sorted(nums)
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                return True
        return False


class OptimalSolution:
    def solve(self, nums: List[int]) -> bool:
        seen: Set[int] = set()
        for value in nums:
            if value in seen:
                return True
            seen.add(value)
        return False


if __name__ == '__main__':
    print(OptimalSolution().solve([1, 2, 3, 1]))

