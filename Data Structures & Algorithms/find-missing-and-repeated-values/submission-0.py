class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums.append(grid[i][j])

        repeated = missing = 0

        seen = set()
        for num in nums:
            if num in seen:
                repeated = num
                break

            seen.add(num)

        for i in range(1, len(grid) ** 2 + 1):
            if i not in nums:
                missing = i
                break

        output = [repeated, missing]

        return output