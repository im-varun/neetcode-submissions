class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {}
        n = len(names)

        for i in range(n):
            hashmap[heights[i]] = names[i]

        heights.sort(reverse=True)
        
        output = []
        for height in heights:
            output.append(hashmap[height])

        return output