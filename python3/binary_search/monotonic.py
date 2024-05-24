from typing import List


def first_not_smaller(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    low, high, fns = 0, len(arr) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            fns = mid
            high = mid - 1
        else:
            low = mid + 1
    return fns


print(first_not_smaller([2, 3, 5, 7, 11, 13, 17, 19], 6))
