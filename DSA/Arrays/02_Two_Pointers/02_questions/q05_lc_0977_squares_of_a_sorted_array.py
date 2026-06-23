"""LeetCode #977 - Squares of a Sorted Array."""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> List[int]:
        return sorted(value * value for value in nums)


class BetterSolution:
    def solve(self, nums: List[int]) -> List[int]:
        negatives = [value * value for value in nums if value < 0][::-1]
        non_negatives = [value * value for value in nums if value >= 0]

        merged: List[int] = []
        i = j = 0
        while i < len(negatives) and j < len(non_negatives):
            if negatives[i] <= non_negatives[j]:
                merged.append(negatives[i])
                i += 1
            else:
                merged.append(non_negatives[j])
                j += 1
        merged.extend(negatives[i:])
        merged.extend(non_negatives[j:])
        return merged


class OptimalSolution:
    def solve(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        left, right = 0, n - 1
        write = n - 1

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square > right_square:
                answer[write] = left_square
                left += 1
            else:
                answer[write] = right_square
                right -= 1
            write -= 1
        return answer

