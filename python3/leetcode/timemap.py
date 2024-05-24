class TimeMap:
    def __init__(self):
        self.histories = dict()

    def set(self, key, value, timestamp: int):
        if not key in self.histories:
            self.histories[key] = []
        self.histories[key].append((timestamp, value))

    def get(self, key: str, timestamp: int):
        if key not in self.histories: return ""
        arr = self.histories.get(key)
        low, high, pos = 0, len(arr) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid][0] <= timestamp:
                pos = mid
                low = mid + 1
            else:
                high = mid - 1
        if pos == -1: return ""
        return arr[pos][1]


timemap = TimeMap()
timemap.set('foo', 'bar', 1)
print(timemap.get('foo', 1))
print(timemap.get('foo', 3))
timemap.set('foo', 'bar2', 4)
print(timemap.get('foo', 4))
print(timemap.get('foo', 5))
