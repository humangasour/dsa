from typing import List


def insertion_sort(array: List[int]):
    for i in range(1, len(array)):
        if array[i] < array[0]:
            array.insert(0, array.pop(i))
        else:
            for j in range(1, i):
                if array[j - 1] < array[i] < array[j]:
                    array.insert(j, array.pop(i))
