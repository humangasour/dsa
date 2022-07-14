import logging

logger = logging.getLogger(name=__name__)


def reverse(string: str) -> str:
    try:
        # get the size of the string/array
        last_index = len(string) - 1
        reversed_str = ''
        for i in range(last_index, 0, -1):
            reversed_str += string[i]
        return reversed_str
    except Exception as ex:
        logger.error(str(ex), exc_info=True)
