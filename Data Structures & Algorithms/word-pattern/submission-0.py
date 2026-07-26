class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        pattern = list(pattern)
        
        if len(pattern) != len(s):
            return False

        pattern_hashmap = {}
        s_hashmap = {}
        for c1, c2 in zip(pattern, s):
            if c1 in pattern_hashmap and pattern_hashmap[c1] != c2:
                return False

            if c2 in s_hashmap and s_hashmap[c2] != c1:
                return False

            pattern_hashmap[c1] = c2
            s_hashmap[c2] = c1

        return True