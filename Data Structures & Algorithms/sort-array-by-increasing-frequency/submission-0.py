class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        nums.sort(key=lambda num: (count[num], -num))
        return nums