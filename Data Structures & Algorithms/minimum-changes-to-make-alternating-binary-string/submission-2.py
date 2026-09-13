class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0
        cmp = 0
        for c in s:
            if int(c) != cmp:
                count1 += 1
            cmp ^= 1

        count2 = 0
        cmp = 1
        for c in s:
            if int(c) != cmp:
                count2 += 1
            cmp ^= 1

        output = min(count1, count2)
        
        return output