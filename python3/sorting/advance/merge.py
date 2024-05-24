import math
from typing import List


# 5, 3, 1, 2, 4
# divide until sorted
# merge the sorted list in one
def merge_sort(unsorted_list: List[int], left: [int], right: [int]) -> List[int]:
    mid = math.floor((right - left) / 2)
    if left == right:
        return unsorted_list

    while left < right:
        left_sorted = merge_sort(unsorted_list, left, mid)
        right_sorted = merge_sort(unsorted_list, mid, right)
        i = left
        j = mid
        merged = []
        while i < j:
            if left_sorted[i] < right_sorted[j]:
                merged.append(left_sorted)
                i += 1
            else:
                merged.append(right_sorted[j])
                j += 1
        return merged

    return unsorted_list


merge_sort([5,3,1,2,4], 0 , 5)
