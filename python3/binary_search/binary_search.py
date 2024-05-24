from typing import List


# 1, 2, 3, 4, 5
def binary_search(array: List[int], target: int) -> int:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = high - low // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(binary_search([1, 2, 3, 4, 5], 1))
