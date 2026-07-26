class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            word = strs[i]
            k = l = 0
            while k < len(prefix) and l < len(word) and prefix[k] == word[l]:
                k += 1
                l += 1

            prefix = word[0:l]
        
        return prefix