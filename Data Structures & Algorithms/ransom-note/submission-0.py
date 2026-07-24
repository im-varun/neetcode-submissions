class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom = Counter(ransomNote)
        count_magazine = Counter(magazine)

        for c in ransomNote:
            if c not in count_magazine or count_ransom[c] > count_magazine[c]:
                return False

        return True