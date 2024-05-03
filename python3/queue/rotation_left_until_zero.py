from typing import List
from collections import deque


def rotate_left_until_zero(nums: List[int]) -> deque[int]:
    queue = deque(nums)
    while queue[0] != 0:
        queue.append(queue.popleft())

    return queue


print(rotate_left_until_zero([1, 2, 0, 5, 6, 8, 0, ]))
