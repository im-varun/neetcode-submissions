class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        majority_count = len(nums) // 2

        for key, value in hashmap.items():
            if value > majority_count:
                return key