from typing import List


def permutation(letters: str) -> List[str]:
    n = len(letters)

    def dfs(stat_index, path, used, res):
        if stat_index == n:
            res.append(''.join(path))
            return

        for i, letter in enumerate(letters):
            if used[i]:
                continue
            path.append(letter)
            used[i] = True
            dfs(stat_index + 1, path, used, res)
            path.pop()
            used[i] = False

    ans = []
    dfs(0, [], [False] * n, ans)
    return ans


print((permutation('abc')))
