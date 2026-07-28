class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map[key]

        output = ""

        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid][0] <= timestamp:
                output = arr[mid][1]
                low = mid + 1
            else:
                high = mid - 1

        return output
