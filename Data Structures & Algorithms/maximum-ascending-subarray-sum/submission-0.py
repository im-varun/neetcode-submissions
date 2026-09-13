class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        output = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                curr_sum = 0

            curr_sum += nums[i]
            output = max(output, curr_sum)

        return output