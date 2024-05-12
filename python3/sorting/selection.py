from typing import List


# [5, 3, 1, 2, 4]
def selection_sort(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(0, n):
        min_index = i
        for j in range(i, n):
            if unsorted_list[min_index] > unsorted_list[j]:
                min_index = j

        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    return unsorted_list


print(selection_sort([5, 3, 1, 2, 4]))
