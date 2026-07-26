class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                hashset.remove(num)
            else:
                hashset.add(num)

        return len(hashset) == 0