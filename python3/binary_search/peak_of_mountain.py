from typing import List


def peak_of_mountain_array(arr: List[int]) -> int:
    n, result = len(arr), -1
    if n < 3:
        return result
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return arr[result]


print(peak_of_mountain_array([0, 1, 2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 133, 132, 111, 0]))
