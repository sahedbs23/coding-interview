# factorial using recursion
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def iterative_factorial(n: int) -> int:
    stack = []
    while n > 0:
        stack.append(n)
        n -= 1
    res = 1

    while stack:
        res *= stack.pop()

    return res


print(factorial(5))
print(iterative_factorial(5))
