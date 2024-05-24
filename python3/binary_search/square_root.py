# def square_root(n: int) -> int:
#     odd = 1
#     sr = 0
#     while n - odd >= 0:
#         n = n - odd
#         odd += 2
#         sr += 1
#
#     return sr


def square_root(n: int) -> int:
    if n == 0:
        return 0

    left, right = 1, n
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res - 1


print(square_root(144))
print(square_root(169))
print(square_root(256))
print(square_root(576))
print(square_root(436))
print(square_root(5))
print(square_root(6))
print(square_root(7))
print(square_root(8))
print(square_root(9))
