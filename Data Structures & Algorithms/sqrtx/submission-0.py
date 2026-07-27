class Solution:
    def mySqrt(self, x: int) -> int:
        output = 0
        low, high = 0, x
        while low <= high:
            middle = low + (high - low) // 2
            if middle * middle > x:
                high = middle - 1
            elif middle * middle < x:
                output = middle
                low = middle + 1
            elif middle * middle == x:
                return middle

        return output