class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)

        output = 0
        for word in words:
            word_count = Counter(word)
            
            good = True
            for key in word_count:
                if word_count[key] > chars_count[key]:
                    good = False
                    break
            
            if good:
                output += len(word)

        return output