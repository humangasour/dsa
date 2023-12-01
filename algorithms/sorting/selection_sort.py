from typing import List


def selection_sort(array: List[int]):
    for i in range(len(array)):
        smallest_index = i
        for j in range(i, len(array)):
            if array[j] < array[smallest_index]:
                smallest_index = j
        array[i], array[smallest_index] = array[smallest_index], array[i]
