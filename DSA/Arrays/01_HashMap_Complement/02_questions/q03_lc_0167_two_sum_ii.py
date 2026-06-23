"""
Question: Two Sum II - Input Array Is Sorted
LeetCode: #167
Difficulty: Medium
Pattern: Two pointers on sorted array
"""

from typing import List


class BruteForce:
    def solve(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []


class BetterSolution:
    def solve(self, numbers: List[int], target: int) -> List[int]:
        # Hash map also works, but uses extra space.
        seen = {}
        for i, value in enumerate(numbers):
            need = target - value
            if need in seen:
                return [seen[need] + 1, i + 1]
            seen[value] = i
        return []


class OptimalSolution:
    def solve(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            if current < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == '__main__':
    print(OptimalSolution().solve([2, 7, 11, 15], 9))

