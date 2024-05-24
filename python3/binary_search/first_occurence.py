from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    l, h, f = 0, len(arr) - 1, -1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == target:
            f = mid
            h = mid - 1
        elif arr[mid] > target:
            h = mid - 1
        else:
            l = mid + 1
    return f


print(find_first_occurrence([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3))
print(find_first_occurrence([2, 3, 5, 7, 11, 13, 17, 19], 6))
