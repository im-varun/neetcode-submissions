class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        if n == 1:
            return [-1]

        output = [0] * n

        for i in range(n - 1):
            output[i] = max(arr[(i + 1):n])

        output[n - 1] = -1

        return output