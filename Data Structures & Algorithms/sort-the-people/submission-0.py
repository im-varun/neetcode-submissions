class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_name = []
        n = len(names)

        for i in range(n):
            height_name.append([heights[i], names[i]])

        height_name.sort(reverse=True)

        output = []
        for pair in height_name:
            output.append(pair[1])

        return output