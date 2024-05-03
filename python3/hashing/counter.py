from typing import List


def get_counter(nums):
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    return counter


print(get_counter([1, 2, 2, 3, 4, 5, 1, 2, 3, ]))
