class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        chars = []

        i = j = 0
        while i < len(word1) and j < len(word2):
            chars.append(word1[i])
            chars.append(word2[i])

            i += 1
            j += 1

        if i < len(word1):
            chars.append(word1[i:len(word1)])

        if j < len(word2):
            chars.append(word2[j:len(word2)])

        output = "".join(chars)

        return output