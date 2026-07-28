class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        counts = {}
        for i in range(n):
            for j in range(n):
                counts[grid[i][j]] = counts.get(grid[i][j], 0) + 1

        repeated = missing = 0
        for i in range(1, n * n + 1):
            if counts.get(i, 0) == 2:
                repeated = i

            if counts.get(i, 0) == 0:
                missing = i

        output = [repeated, missing]

        return output