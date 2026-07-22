class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.checkIsomorphic(s, t) and self.checkIsomorphic(t, s)

    def checkIsomorphic(self, s1: str, s2: str) -> bool:
        hashmap = {}
        for c1, c2 in zip(s1, s2):
            if c1 in hashmap:
                if hashmap[c1] != c2:
                    return False
            else:
                hashmap[c1] = c2

        return True