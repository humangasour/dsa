import logging

from stacks.stacks_linked_list import Stack

logger = logging.getLogger(name=__name__)

if __name__ == '__main__':
    try:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        print(stack)
        stack.pop()
        stack.print_stack()
    except Exception as ex:
        logger.error(str(ex), exc_info=True)
