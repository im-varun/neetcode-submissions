class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)

        word1, word2 = strs[0], strs[len(strs) - 1]
        k = l = 0
        while k < len(word1) and l < len(word2) and word1[k] == word2[l]:
            k += 1
            l += 1

        output = word1[0:l]

        return output