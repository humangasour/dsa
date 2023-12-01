from typing import List


def merge_sort(array: List[int]) -> List[int]:
    if len(array) == 1:
        return array

    middle_index = len(array) // 2
    left = array[:middle_index]
    right = array[middle_index:]

    return merge(
            merge_sort(left),
            merge_sort(right)
    )


def merge(left_array: List[int], right_array: List[int]) -> List[int]:
    sorted_array = []
    left_index = 0
    right_index = 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            sorted_array.append(left_array[left_index])
            left_index += 1
        else:
            sorted_array.append(right_array[right_index])
            right_index += 1

    return sorted_array + left_array[left_index:] + right_array[right_index:]
