class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_cleaned = "".join(char for char in s_lower if char.isalnum())

        low, high = 0, len(s_cleaned) - 1
        while low < high:
            if s_cleaned[low] == s_cleaned[high]:
                low += 1
                high -= 1
            else:
                return False

        return True