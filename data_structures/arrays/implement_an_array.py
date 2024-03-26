import logging

logger = logging.getLogger(__name__)


class MyArray(object):

    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index: int) -> str:
        try:
            return self.data[index]
        except KeyError as ex:
            logger.error(str(f'key {ex} does not exist in array'), exc_info=False)
        except Exception as ex:
            logger.error(str({ex}), exc_info=True)

    def push(self, item: str):
        self.data[self.length] = item
        self.length += 1

    def pop(self, index: int = None) -> str:
        try:
            if not index:
                index = self.length - 1
            item = self.get(index)
            del self.data[index]
            if index != self.length - 1:
                self.__shift_items(index)
            self.length -= 1
            return item
        except Exception as ex:
            logger.error(str({ex}), exc_info=True)

    def __shift_items(self, index: int):
        try:
            for i in range(index, self.length - 1):
                self.data[i] = self.data[i+1]
            del self.data[self.length - 1]
        except Exception as ex:
            logger.error(str({ex}), exc_info=True)



