from typing import Any, Optional


class Node:
    """
    A node in a queue.

    Attributes:
        value (Any): The value stored in the node.
        next (Optional[Node]): The reference to the next node in the queue, or None if this is the last node.
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


class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.front = None
        self.rear = None
        self.length = 0

    def peek(self) -> Any:
        """
        Return the value of the front item in the queue without removing it.

        Returns:
            Any: The value of the front item.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.front is not None:
            return self.front.value
        raise IndexError("Peek from an empty queue")

    def enqueue(self, value: Any) -> None:
        """
        Add a new item with the specified value to the end of the queue.

        Args:
            value (Any): The value to add to the queue.
        """
        new_node = Node(value)

        if self.length == 0:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def dequeue(self) -> Any:
        """
        Remove and return the item at the front from the queue.

        Returns:
            Any: The value of the removed item.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.front is not None:
            removed_value = self.front.value
            self.front = self.front.next
            if self.front is None:  # This handles the case of removing the last element
                self.rear = None
            self.length -= 1
            return removed_value
        raise IndexError("Dequeue from an empty queue")

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.length == 0

    def __str__(self) -> str:
        """
        Create a string representation of the queue.

        Returns:
            str: A string representing the queue.
        """
        elements = []
        current = self.front
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)
