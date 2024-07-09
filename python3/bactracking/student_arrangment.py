class StudentArrangement:
    def __init__(self):
        self.seats = ['q1']
        self.s_len = 4
        self.answer = []
        self.row, self.col = 4, 4

    def dfs(self, start_index, path):
        if start_index == self.s_len:
            # print(path)
            # self.answer.append(''.join(path))
            return

        # for seat in iter(self.seats):
        for row in range(start_index, self.row):
            for col in range(start_index, self.col):
                print(path)
                if [row, col] in path or [row, col - 1] in path or [row, col + 1] in path:
                    pass
                else:
                    path.append([row, col])
                    self.dfs(start_index + 1, path)
                    path.pop()


arrangement = StudentArrangement()
arrangement.dfs(0, [])
print(arrangement.answer)
print(len(arrangement.answer))

# 0-> 0 1 2 3
# 1-> 0 1 2 3
# 2-> 0 1 2 3
# 3-> 0 1 2 3
