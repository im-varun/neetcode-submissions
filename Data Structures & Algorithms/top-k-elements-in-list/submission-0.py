class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        arr = []
        for num, count in hashmap.items():
            arr.append([count, num])

        arr.sort()

        output = []
        while len(output) < k:
            output.append(arr.pop()[1])

        return output