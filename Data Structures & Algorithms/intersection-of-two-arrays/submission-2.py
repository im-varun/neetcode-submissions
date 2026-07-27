class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        for num in nums1:
            seen[num] = 1

        output = []
        for num in nums2:
            if seen.get(num, 0) == 1:
                output.append(num)
                seen[num] = 0

        return output