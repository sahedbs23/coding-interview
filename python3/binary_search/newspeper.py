# 1 < read time length < 10^5
# 1 < newspaper[i] read time  < 10^5
# 1 < number of coworkers < 10^5
# can't pick random, must be consecutive
from typing import List


def feasible(newspapers_read_times: List[int], num_coworkers: int, limit: int) -> bool:
    time, workers = 0, 0
    for newspaper_read_time in newspapers_read_times:
        if time + newspaper_read_time > limit:
            time = 0
            workers += 1
        time += newspaper_read_time
    if time != 0:
        workers += 1
    return workers <= num_coworkers


def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    left = max(newspapers_read_times)
    right = sum(newspapers_read_times)
    r = -1
    while left <= right:
        mid = (left + right) // 2
        if feasible(newspapers_read_times, num_coworkers, mid):
            r = mid
            right = mid - 1
        else:
            left = mid + 1
    return r


print(newspapers_split([7, 2, 5, 10, 8], 2))
print(newspapers_split([2, 3, 5, 7], 3))
