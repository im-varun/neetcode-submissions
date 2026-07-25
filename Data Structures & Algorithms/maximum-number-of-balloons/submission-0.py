class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        balloon = Counter("balloon")

        output = len(text)
        for c in balloon:
            output = min(output, count[c] // balloon[c])

        return output