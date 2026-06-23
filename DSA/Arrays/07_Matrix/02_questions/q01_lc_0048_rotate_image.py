"""LeetCode #48 - Rotate Image."""
from typing import List


class BruteForce:
    def solve(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                rotated[c][n - 1 - r] = matrix[r][c]
        for r in range(n):
            for c in range(n):
                matrix[r][c] = rotated[r][c]


class BetterSolution:
    def solve(self, matrix: List[List[int]]) -> None:
        OptimalSolution().solve(matrix)


class OptimalSolution:
    def solve(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

