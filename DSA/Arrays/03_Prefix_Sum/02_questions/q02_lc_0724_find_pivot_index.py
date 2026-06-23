"""LeetCode #724 - Find Pivot Index."""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


class BetterSolution:
    def solve(self, nums: List[int]) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        for i in range(len(nums)):
            left_sum = prefix[i]
            right_sum = prefix[-1] - prefix[i + 1]
            if left_sum == right_sum:
                return i
        return -1


class OptimalSolution:
    def solve(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for index, value in enumerate(nums):
            right_sum = total - left_sum - value
            if left_sum == right_sum:
                return index
            left_sum += value
        return -1

