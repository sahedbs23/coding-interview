from typing import List


def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == target:
            return [i, j]
        elif arr[i] + arr[j] > target:
            j -= 1
        else:
            i += 1

    return []
