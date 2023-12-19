from typing import Any


class Stack:
    """
    A simple implementation of a stack data structure using an array.

    This stack implementation uses a Python list to store elements. It offers
    Last-In-First-Out (LIFO) access to elements. The stack dynamically resizes
    as elements are added or removed.

    Attributes:
        _stack (List[Any]): The list to store stack elements.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self._stack = []

    def peek(self) -> Any:
        """
        Return the value of the top item in the stack without removing it.

        Returns:
            Any: The value of the top item, or None if the stack is empty.
        """
        if not self.is_empty():
            return self._stack[-1]
        return None

    def push(self, value: Any) -> None:
        """
        Add a new item with the specified value to the top of the stack.

        Args:
            value (Any): The value to add to the stack.
        """
        self._stack.append(value)

    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.

        Returns:
            Any: The value of the removed item, or None if the stack is empty.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self._stack.pop()
        raise IndexError("Pop from an empty stack")

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._stack) == 0

    def __str__(self) -> str:
        """
        Return a string representation of the stack.

        Returns:
            str: A string representing the stack's contents.
        """
        return ' -> '.join(map(str, reversed(self._stack))) if self._stack else 'Empty Stack'

    def size(self) -> int:
        """
        Return the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self._stack)
