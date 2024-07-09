from typing import List


def word_break(s: str, words: List[str]) -> bool:
    n = len(words)
    memo = {}

    def dfs(start_index):
        if start_index == len(s):
            return True
        if start_index in memo:
            return memo[start_index]
        ans = False
        for word in words:
            if s[start_index:].startswith(word):
                if dfs(start_index + len(word)):
                    ans = True
                    break

        memo[start_index] = ans
        return ans

    return dfs(0)


if __name__ == '__main__':
    s = input()
    words = input().split()
    res = word_break(s, words)
    print('true' if res else 'false')
