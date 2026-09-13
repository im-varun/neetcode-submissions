class Solution:
    def largestGoodInteger(self, num: str) -> str:
        output = ""
        val = 0
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                string = num[i:(i + 3)]
                if int(string) >= val:
                    val = int(string)
                    output = string

        return output