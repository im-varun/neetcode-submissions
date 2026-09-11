# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

import random

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n

        while True:
            my_guess = random.randint(start, end)
            result = guess(my_guess)
            if result == -1:
                end = my_guess - 1
            elif result == 1:
                start = my_guess + 1
            else:
                return my_guess