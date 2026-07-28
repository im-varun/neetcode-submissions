class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {}

        if timestamp not in self.map[key]:
            self.map[key][timestamp] = []

        self.map[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        latest = 0
        for time in self.map[key]:
            if time <= timestamp:
                latest = max(latest, time)

        output = "" if latest == 0 else self.map[key][latest][-1]

        return output
