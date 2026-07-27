class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)

        threshold = len(nums) // 3
        
        output = []
        for key in counts:
            if counts[key] > threshold:
                output.append(key)

        return output