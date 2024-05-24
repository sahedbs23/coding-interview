from typing import List


# 5, 3, 2, 1
def iterative_merge(array: List[int]):
    n = len(array)
    # size of each list
    current_arr_size = 1

    # loop until size of arr become full lists size
    while current_arr_size < n:
        left = 0

        while left < n - 1:
            mid = min(left + current_arr_size - 1, n - 1)
            right = min(left + 2 * current_arr_size - 1, n - 1)
            merge(array, left, mid, right)
            left += 2 * current_arr_size

        current_arr_size *= 2


# arr, 0, 0, 1
# arr , 2, 2, 3
def merge(array, left, mid, right):
    ll = mid - left + 1
    rl = right - mid

    la = array[left: mid + 1]
    ra = array[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < ll and j < rl:
        if la[i] > ra[j]:
            array[k] = ra[j]
            j += 1
        else:
            array[k] = la[i]
            i += 1

        k += 1

    while i < ll:
        array[k] = la[i]
        i += 1
        k += 1

    while j < rl:
        array[k] = ra[j]
        j += 1
        k += 1


arr = [12, 11, 13, 5, 6, 7]
iterative_merge(arr)
print(arr)
