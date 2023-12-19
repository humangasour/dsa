from typing import Any


class Queue:
    """
    A queue implementation using two stacks.

    This queue supports basic queue operations including enqueue, dequeue,
    and peek, while internally maintaining two stacks to manage the order of elements.

    Attributes:
        stack_in (list): A stack used for enqueuing elements.
        stack_out (list): A stack used for dequeuing elements.
    """

    def __init__(self):
        """Initializes the queue with two empty stacks."""
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, value: Any):
        """
        Adds an element to the back of the queue.

        Args:
            value (Any): The element to be added to the queue.
        """
        self.stack_in.append(value)

    def dequeue(self) -> Any:
        """
        Removes and returns the element from the front of the queue.

        Returns:
            Any: The element at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue is not allowed.")

        if len(self.stack_out) == 0:
            self._move_elements_from_stack_in_to_stack_out()
        return self.stack_out.pop()

    def peek(self) -> Any:
        """
        Returns the element at the front of the queue without removing it.

        Returns:
            Any: The element at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue is not allowed.")

        if len(self.stack_out) == 0:
            self._move_elements_from_stack_in_to_stack_out()
        return self.stack_out[-1]

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.stack_in) == 0 and len(self.stack_out) == 0

    def _move_elements_from_stack_in_to_stack_out(self):
        """Moves elements from stack_in to stack_out to maintain queue order."""
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
