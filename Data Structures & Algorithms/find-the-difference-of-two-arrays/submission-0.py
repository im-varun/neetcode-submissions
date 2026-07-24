class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums_set1 = set(nums1)
        nums_set2 = set(nums2)

        ans = []

        ans_0 = []
        for num in nums_set1:
            if num not in nums_set2:
                ans_0.append(num)
        ans.append(ans_0)

        ans_1 = []
        for num in nums_set2:
            if num not in nums_set1:
                ans_1.append(num)
        ans.append(ans_1)

        return ans