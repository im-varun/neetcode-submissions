class Solution:
    def minOperations(self, s: str) -> int:
        output = 0
        cmp = s[0]
        for i in range(len(s)):
            if s[i] != cmp:
                output += 1
            cmp = "1" if cmp == "0" else "0"

        return min(output, len(s) - output)