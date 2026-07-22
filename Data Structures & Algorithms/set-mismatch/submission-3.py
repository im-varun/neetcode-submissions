class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = [0] * (len(nums) + 1)
        for num in nums:
            counts[num] += 1

        missing, duplicate = 0, 0
        for i in range(1, len(nums) + 1):
            if counts[i] == 0:
                missing = i
            if counts[i] == 2:
                duplicate = i

        return [duplicate, missing]