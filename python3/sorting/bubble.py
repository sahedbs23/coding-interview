from typing import List


# 5, 3, 1, 2, 4
# 3, 1, 2, 4, 5
# 1, 2, 3, 4, 5
#
# compare first with the next
# if next is smaller than first one swap the value
# and update that swap happened

# loop throw first until last sorted
# loop
def bubble_sort(unsorted_list: [List[int]]) -> List[int]:
    for i in reversed(range(len(unsorted_list))):
        swapped = False
        for j in range(i):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
                swapped = True
        if not swapped:
            return unsorted_list
    return unsorted_list


print(bubble_sort([5, 3, 1, 2, 4]))
