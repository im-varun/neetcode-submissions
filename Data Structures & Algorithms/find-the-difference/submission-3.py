class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap_s, hashmap_t = {}, {}

        for c in s:
            hashmap_s[c] = hashmap_s.get(c, 0) + 1

        for c in t:
            hashmap_t[c] = hashmap_t.get(c, 0) + 1

        for key, value in hashmap_t.items():
            if key not in hashmap_s:
                return key

            if value > hashmap_s[key]:
                return key