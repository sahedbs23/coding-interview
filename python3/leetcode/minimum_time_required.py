from typing import List


def feasible(jobs: List[int], k: int, t: int):
    worker, time = 0, 0
    for job in jobs:
        if time + job > t:
            time = 0
            worker += 1
        time += job
    if time != 0:
        worker += 1
    return worker <= k


def minimumTimeRequired(jobs: List[int], k: int) -> int:
    low = max(jobs)
    high = sum(jobs)
    r = -1
    while low <= high:
        mid = (low + high) // 2
        if feasible(jobs, k, mid):
            r = mid
            high = mid - 1
        else:
            low = mid + 1
    return r


# print(minimumTimeRequired([3, 2, 3], 3))
print(minimumTimeRequired([1, 2, 4, 7, 8], 2))
