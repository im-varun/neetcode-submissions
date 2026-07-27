class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        max_product = nums[n - 1] * nums[n - 2]
        min_product = nums[0] * nums[1]

        difference = max_product - min_product

        return difference