class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        output = float("inf")
        l, r = 0, k - 1
        while r < len(nums):
            diff = nums[r] - nums[l]
            output = min(output, diff)
            l += 1
            r += 1

        return output