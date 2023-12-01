def iterative_fibonacci(n: int) -> int:
    output_arr = []
    for i in range(n+1):
        if i < 2:
            output_arr.append(i)
        else:
            output_arr.append(output_arr[i - 1] + output_arr[i - 2])
    return output_arr[-1]


def recursive_fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
