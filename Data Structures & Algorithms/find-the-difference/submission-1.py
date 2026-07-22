from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
      extra = Counter(t) - Counter(s)
      return list(extra.keys())[0]