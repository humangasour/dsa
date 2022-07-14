import logging

logger = logging.getLogger(name=__name__)


def merge_sorted_arrays(arr_1: list[int], arr_2: list[int]) -> list[int]:
    try:
        # check the types of list
        if not isinstance(arr_1, list):
            raise TypeError('argument 1 should a list')

        if not isinstance(arr_2, list):
            raise TypeError('argument 2 should a list')

        merged_array = arr_1 + arr_2

        if len(arr_1) == 0 or len(arr_2) == 0:
            return merged_array

        merged_array.sort()
        return merged_array
    except TypeError as ex:
        logger.error(str(ex))
    except Exception as ex:
        logger.error(str(ex), exc_info=True)


def merge_sorted_arrays_2(arr_1: list[int], arr_2: list[int]) -> list[int]:
    try:
        # check the types of list
        if not isinstance(arr_1, list):
            raise TypeError('argument 1 should a list')

        if not isinstance(arr_2, list):
            raise TypeError('argument 2 should a list')

        len_1 = len(arr_1)
        len_2 = len(arr_2)

        if len_1 == 0 or len_2 == 0:
            return arr_1 + arr_2

        i = 0
        j = 0
        merged_arr = []

        while i < len_1 and j < len_2:
            if arr_1[i] <= arr_2[j]:
                merged_arr.append(arr_1[i])
                i += 1
            elif arr_2[j] < arr_1[i]:
                merged_arr.append(arr_2[j])
                j += 1
        return merged_arr + arr_1[i:] + arr_2[j:]

    except TypeError as ex:
        logger.error(str(ex))
    except Exception as ex:
        logger.error(str(ex), exc_info=True)
