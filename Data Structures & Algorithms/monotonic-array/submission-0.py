class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)

        is_increasing = True
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                is_increasing = False
                break

        if is_increasing:
            return True

        is_decreasing = True
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                is_decreasing = False
                break

        return True if is_decreasing else False