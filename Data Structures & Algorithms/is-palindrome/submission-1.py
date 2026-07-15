class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_cleaned = "".join(char for char in s_lower if char.isalnum())

        return s_cleaned == s_cleaned[::-1]