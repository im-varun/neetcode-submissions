from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = []
        for num in nums:
            arr.append(str(num))

        def custom_compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(arr, key=cmp_to_key(custom_compare))
        output = "".join(nums)

        return "0" if output[0] == "0" else output