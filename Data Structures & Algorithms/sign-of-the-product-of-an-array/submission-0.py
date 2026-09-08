class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num

        return self.signFunc(product)
        
    def signFunc(self, x):
        if x == 0:
            return 0

        if x > 0:
            return 1
        else:
            return -1