from typing import Any, Optional


class Node:
    """
    A node in a stack.

    Attributes:
        value (Any): The value stored in the node.
        next (Optional[Node]): The reference to the next node in the stack, or None if this is the last node.
    """

    def __init__(self, value: Any):
        """
        Initialize a Node with a given value.

        Args:
            value (Any): The value to be stored in the node.
        """
        self.value = value
        self.next: Optional[Node] = None

    def __str__(self) -> str:
        """
        Create a string representation of the node.

        Returns:
            str: A string representing the node and its link to the next node.
        """
        return f"Node({self.value}) -> {('Node(' + str(self.next.value) + ')' if self.next else 'None')}"


class Stack:
    """
    A simple implementation of a stack data structure.

    A stack is a collection of elements with two principal operations:
    push, which adds an element to the collection, and pop, which removes
    the most recently added element. This implementation uses a linked list
    structure to allow for dynamic memory allocation.

    Attributes:
        top (Optional[Node]): The top node of the stack.
        length (int): The number of elements in the stack.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.top = None
        self.length = 0

    def peek(self) -> Any:
        """
        Return the value of the top item in the stack without removing it.

        Returns:
            Any: The value of the top item, or None if the stack is empty.
        """
        if self.top is not None:
            return self.top.value
        return None

    def push(self, value: Any) -> None:
        """
        Add a new item with the specified value to the top of the stack.

        Args:
            value (Any): The value to add to the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.

        Returns:
            Any: The value of the removed item, or None if the stack is empty.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.top is not None:
            removed_value = self.top.value
            self.top = self.top.next
            self.length -= 1
            return removed_value
        raise IndexError("Pop from an empty stack")

    def __str__(self) -> str:
        """
        Return a string representation of the stack.

        Returns:
            str: A string representing the stack's contents.
        """
        current = self.top
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
        return ' -> '.join(result) if result else 'Empty Stack'

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.length == 0
