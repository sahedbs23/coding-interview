from typing import List


def quick_sort(unsorted_lists: List[int], start: int, end: int):
    # if only one element or less than one, already sorted
    if end - start <= 1:
        return

    pivot = unsorted_lists[end - 1]
    start_pointer, end_pointer = start, end - 1

    while start_pointer < end_pointer:
        while unsorted_lists[start_pointer] < pivot and start_pointer < end_pointer:
            start_pointer += 1

        while unsorted_lists[end_pointer] >= pivot and start_pointer < end_pointer:
            end_pointer -= 1

        unsorted_lists[start_pointer], unsorted_lists[end_pointer] = unsorted_lists[end_pointer], unsorted_lists[start_pointer]

    unsorted_lists[end_pointer], unsorted_lists[end - 1] = unsorted_lists[end - 1], unsorted_lists[end_pointer]

    quick_sort(unsorted_lists, start, end_pointer)
    quick_sort(unsorted_lists, end_pointer+1, end)


unordered_lists = [5, 3, 1, 2, 4]
quick_sort(unordered_lists, 0, len(unordered_lists))
print(unordered_lists)