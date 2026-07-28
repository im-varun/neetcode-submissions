class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            output.append(num ** 2)

        output.sort()

        return output