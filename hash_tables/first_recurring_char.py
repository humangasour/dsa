from typing import List, Union


def first_recurring_char(arr: List[int]) -> Union[int, None]:
    # [2, 5, 1, 2, 3, 1, 5, 4, 2, 8] -> 2
    # [2, 1, 1, 2, 3, 5, 1, 2, 4] -> 1
    # [2, 3, 4, 5] -> None
    if len(arr) < 2:
        return None

    items = set()
    for i, item in enumerate(arr):
        if item in items:
            return item
        items.add(item)
    return None


def naive_first_recurring_char(arr: List[int]) -> Union[int, None]:
    # [2, 5, 1, 5, 2, 3, 1, 5, 4, 2, 8] -> 5
    if len(arr) < 2:
        return None

    length = len(arr)
    result = None
    for i in range(length):
        for j in range(i + 1, length):
            if arr[i] == arr[j]:
                length = j
                result = arr[j]

    return result
