class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sums, right_sums = {}, {}

        n = len(nums)

        left = 0
        for i in range(n):
            left_sums[i] = left
            left += nums[i]

        right = 0
        for i in range(n - 1, -1, -1):
            right_sums[i] = right
            right += nums[i]

        for index in left_sums:
            if left_sums[index] == right_sums[index]:
                return index

        return -1