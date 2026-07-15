class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = []
        for i, value in enumerate(nums):
            value_index.append([value, i])

        value_index.sort()
        
        low, high = 0, len(value_index) - 1
        while low < high:
            sum = value_index[low][0] + value_index[high][0]
            if sum == target:
                min_index = min(value_index[low][1], value_index[high][1])
                max_index = max(value_index[low][1], value_index[high][1])
                return [min_index, max_index]
            elif sum < target:
                low += 1
            else:
                high -= 1