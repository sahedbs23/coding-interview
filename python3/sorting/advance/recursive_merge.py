from typing import List


# [12, 11, 13, 5, 6, 7]
# [11, 12, 13] [5, 6, 7]
# [5,6,7,11,12,13]
def merge_sort_recursive(unsorted_list: List[int], left, right):
    n = right - left
    if n <= 1:
        return

    mid = int((left + right) / 2)

    merge_sort_recursive(unsorted_list, left, mid)

    merge_sort_recursive(unsorted_list, mid + 1, right)

    merge(unsorted_list, left, mid, right)


# [12, 11, 13, 5, 6, 7]
def merge(unsorted_lists, left, mid, right):
    las = mid - left
    ras = right - mid

    la = unsorted_lists[left:mid]
    ra = unsorted_lists[mid:right]

    i = j = 0
    k = left

    while i < las and j < ras:
        if la[i] > ra[j]:
            unsorted_lists[k] = ra[j]
            j += 1
        else:
            unsorted_lists[k] = la[i]
            i += 1

        k += 1

    while i < las:
        unsorted_lists[k] = la[i]
        i += 1
        k += 1

    while j < ras:
        unsorted_lists[k] = ra[j]
        j += 1
        k += 1


def sort_algo_way(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)

    if n <= 1:
        return unsorted_list

    mid = n // 2
    left_unsorted, right_unsorted = unsorted_list[:mid], unsorted_list[mid:]
    sorted_list = []

    left_pointer = right_pointer = 0

    while left_pointer < len(left_unsorted) and right_pointer < len(right_unsorted):
        if left_unsorted[left_pointer] > right_unsorted[right_pointer]:
            sorted_list.append(right_unsorted[right_pointer])
            right_pointer += 1
        else:
            sorted_list.append(left_unsorted[left_pointer])
            left_pointer += 1

    while left_pointer < len(left_unsorted):
        sorted_list.append(left_unsorted[left_pointer])
        left_pointer += 1

    while right_pointer < len(right_unsorted):
        sorted_list.append(right_unsorted[right_pointer])
        right_pointer += 1

    return sorted_list


array = [12, 11, 13, 5, 6, 7]
merge_sort_recursive(array, 0, len(array))
print(array)

print(sort_algo_way(array))
