class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {}
        for c in text:
            if c in "balon":
                hashmap[c] = hashmap.get(c, 0) + 1

        if len(hashmap) < 5:
            return 0

        hashmap["l"] = hashmap["l"] // 2
        hashmap["o"] = hashmap["o"] // 2

        output = min(hashmap.values())

        return output