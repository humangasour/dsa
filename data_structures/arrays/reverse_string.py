import logging

logger = logging.getLogger(name=__name__)


def reverse(string: str) -> str:
    try:
        # get the size of the string/array
        last_index = len(string) - 1
        reversed_str = ''
        for i in range(last_index, -1, -1):
            reversed_str += string[i]
        return reversed_str
    except Exception as ex:
        logger.error(str(ex), exc_info=True)


# more readable approach
def reverse_faster(string: str) -> str:
    try:
        return ''.join(reversed(string))
    except Exception as ex:
        logger.error(str(ex), exc_info=True)


# most pythonic approach
def reverse_fastest(string: str) -> str:
    try:
        return string[::-1]
    except Exception as ex:
        logger.error(str(ex), exc_info=True)


# time complexity - O(n)
# space complexity - O(n)
# same for all three approaches
