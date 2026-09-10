class Solution:
    def isPalindrome(self, x: int) -> bool:
        orig = x
        reverse = 0

        while x > 0:
            remainder = x % 10
            reverse = reverse * 10 + remainder
            x = x // 10

        return orig == reverse