class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}

        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1

        largest = -1
        for key, value in hashmap.items():
            if key == value and key > largest:
                largest = key

        return largest