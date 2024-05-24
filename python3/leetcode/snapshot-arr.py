class SnapshotArray:
    def __init__(self, length: int):
        self.histories = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def print(self):
        print(self.histories)

    def set(self, index, value):
        self.histories[index].append([self.snap_id, value])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        left, right, pos = 0, len(self.histories[index]) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if self.histories[index][mid][0] <= snap_id:
                left = mid + 1
                pos = mid
            else:
                right = mid - 1
        return self.histories[index][pos][1]


arr = SnapshotArray(3)
arr.set(0, 5)
arr.set(2, 8)
arr.snap()
arr.set(0, 6)
arr.set(2, 50)

print(arr.get(0, 0))
print(arr.get(2, 1))
