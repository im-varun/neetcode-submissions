class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(n + 1):
            count, num = 0, i
            while num > 0:
                bit = num & 1
                if bit == 1:
                    count += 1

                num >>= 1

            output[i] = count

        return output