import logging

from algorithms.sorting.merge_sort import merge_sort

logger = logging.getLogger(name=__name__)

if __name__ == '__main__':
    try:
        array = [99, 44, 6, 2, 1, 5, 63, 87, 243, 4, 0]
        print(array)
        print(merge_sort(array))
    except Exception as ex:
        logger.error(str(ex), exc_info=True)
