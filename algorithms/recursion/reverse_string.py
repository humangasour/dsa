def recursive_reverse_string(input_str: str) -> str:
    if len(input_str) == 1:
        return input_str
    return input_str[-1] + recursive_reverse_string(input_str[0:-1])


def iterative_reverse_string(input_str: str) -> str:
    output_str = ''
    for i in range(len(input_str)):
        output_str += input_str[len(input_str) - i - 1]
    return output_str
