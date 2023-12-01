def recursive_factorial(num: int) -> int:
    if num == 2:
        return 2
    return num * recursive_factorial(num - 1)


def iterative_factorial(num: int) -> int:
    output = num
    if 0 < num < 3:
        output = num
    for i in range(2, num):
        output *= i
    return output
