"""LeetCode #1480 - Running Sum of 1D Array."""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            answer.append(sum(nums[: i + 1]))
        return answer


class BetterSolution:
    def solve(self, nums: List[int]) -> List[int]:
        return OptimalSolution().solve(nums)


class OptimalSolution:
    def solve(self, nums: List[int]) -> List[int]:
        running = 0
        answer: List[int] = []
        for value in nums:
            running += value
            answer.append(running)
        return answer

