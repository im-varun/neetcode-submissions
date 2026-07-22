class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for digit in digits:
            number = number * 10 + digit

        number += 1

        output = []
        for c in str(number):
            output.append(int(c))

        return output