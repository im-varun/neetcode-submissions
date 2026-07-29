class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for word in words:
            current_count = Counter(word)
            for c in count:
                count[c] = min(count[c], current_count[c])

        output = []
        for c in count:
            for i in range(count[c]):
                output.append(c)

        return output