class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        prefix_products = [0] * length
        suffix_products = [0] * length
        output = [0] * length

        prefix_products[0] = 1
        suffix_products[length - 1] = 1

        for i in range(1, length):
            prefix_products[i] = nums[i - 1] * prefix_products[i - 1]

        for i in range(length - 2, -1, -1):
            suffix_products[i] = nums[i + 1] * suffix_products[i + 1]

        for i in range(length):
            output[i] = prefix_products[i] * suffix_products[i]

        return output