from typing import List


def find_boundary(arr: List[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    low, high, first_true = 0, len(arr) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]:
            first_true = mid
            high = mid - 1
        elif not mid:
            low = mid + 1
        else:
            high = mid - 1

    return first_true


print(find_boundary([False, False, True, True, True]))
