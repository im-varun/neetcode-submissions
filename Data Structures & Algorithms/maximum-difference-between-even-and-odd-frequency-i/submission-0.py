class Solution:
    def maxDifference(self, s: str) -> int:
        count = collections.Counter(s)
        evens = {}
        odds = {}

        for key, value in count.items():
            if value % 2 == 0:
                evens[key] = value
            else:
                odds[key] = value

        freq1 = max(odds.values())
        freq2 = min(evens.values())
        diff = freq1 - freq2

        return diff