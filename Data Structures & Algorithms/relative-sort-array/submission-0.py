class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = {}
        for num in arr1:
            counts[num] = counts.get(num, 0) + 1

        main = []
        for num in arr2:
            count = counts[num]
            for _ in range(count):
                main.append(num)

            del counts[num]

        non_main = []
        for num, count in counts.items():
            for _ in range(count):
                non_main.append(num)
        non_main.sort()

        output = main + non_main

        return output