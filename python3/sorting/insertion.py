from typing import List


# 5, 3, 1, 2, 4
def insertion_sort(unsorted_list: [List[int]]) -> List[int]:
    for index, value in enumerate(unsorted_list):
        current = index
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1

    return unsorted_list


print(insertion_sort([5, 3, 1, 2, 4]))
