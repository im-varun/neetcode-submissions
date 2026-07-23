class Solution:
    def maxDifference(self, s: str) -> int:
        count = collections.Counter(s)
        odd_max, even_min = 0, len(s)

        for cnt in count.values():
            if cnt % 2 == 0:
                even_min = min(even_min, cnt)
            else:
                odd_max = max(odd_max, cnt)

        return odd_max - even_min