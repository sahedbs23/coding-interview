from typing import List


def partition(s: str) -> List[List[str]]:
    ans = []
    n = len(s)

    def is_palindrome(word: str):
        return word == word[::-1]

    def dfs(start, current_path):
        if start == n:
            ans.append(current_path[:])
            return

        for end in range(start + 1, n + 1):
            prefix = s[start:end]
            if is_palindrome(prefix):
                dfs(end, current_path + [prefix])

    dfs(0, [])
    return ans


if __name__ == '__main__':
    s = input()
    res = partition(s)
    for row in res:
        print(' '.join(row))
