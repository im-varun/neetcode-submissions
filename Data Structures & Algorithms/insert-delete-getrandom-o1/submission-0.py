class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val] = val
        self.size += 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        self.map.pop(val)
        self.size -= 1

        return True

    def getRandom(self) -> int:
        index = random.randint(0, self.size - 1)
        keys = list(self.map.keys())
        return keys[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()