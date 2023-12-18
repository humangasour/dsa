from typing import Any, Optional


class Node:
    """
    A node in a doubly linked list.

    Attributes:
        value (Any): The value stored in the node.
        next (Optional[Node]): The reference to the next node in the doubly linked list, or None if this is the last node.
        previous (Optional[Node]): The reference to the previous node in the doubly linked list, or None if this is the first node.
    """

    def __init__(self, value: Any):
        """
        Initialize a Node with a given value.

        Args:
            value (Any): The value to be stored in the node.
        """
        self.value = value
        self.next: Optional[Node] = None
        self.previous: Optional[Node] = None

    def __str__(self) -> str:
        """
        Create a string representation of the node.

        Returns:
            str: A string representing the node and its links to the next and previous nodes.
        """
        prev_value = f"Previous Node({self.previous.value})" if self.previous else "None"
        next_value = f"Node({self.next.value})" if self.next else "None"
        return f"{prev_value} <- Node({self.value}) -> {next_value}"


class DoublyLinkedList:
    """
    A doubly linked list data structure.

    Attributes:
        head (Optional[Node]): The first node in the linked list, or None if the list is empty.
        tail (Optional[Node]): The last node in the linked list, or None if the list is empty.
        length (int): The number of nodes in the linked list.
    """

    def __init__(self, value: Any):
        """
        Initialize a LinkedList with a single node.

        Args:
            value (Any): The value for the initial node in the linked list.
        """
        initial_node = Node(value)
        self.head = initial_node
        self.tail = initial_node
        self.length = 1

    def __str__(self) -> str:
        """
        Create a string representation of the doubly linked list.

        Returns:
            str: A string representing the doubly linked list.
        """
        node_values = []
        current_node = self.head
        while current_node:
            node_values.append(str(current_node.value))
            current_node = current_node.next
        return ' -> '.join(node_values)

    def append(self, value: Any):
        """
        Append a new node with the given value to the end of the doubly linked list.

        If the list is empty, the new node becomes both the head and the tail of the list. Otherwise, it's added after the current tail.

        Args:
            value (Any): The value for the new node to be appended.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        print(self)

    def prepend(self, value: Any):
        """
        Prepend a new node with the given value to the start of the doubly linked list.

        If the list is empty, the new node becomes both the head and the tail of the list. Otherwise, it's added before the current head.

        Args:
            value (Any): The value for the new node to be prepended.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
        print(self)

    def insert(self, index: int, value: int):
        """
        Insert a new node with the given value at the specified index in the doubly linked list.

        Args:
            index (int): The index before which the new node will be inserted.
            value (Any): The value of the new node to be inserted.

        Raises:
            TypeError: If the index is not an integer.
            ValueError: If the index is out of the bounds of the doubly linked list.
        """
        if not isinstance(index, int) or index < 0:
            raise TypeError('The index must be a non-negative integer')

        if index >= self.length:
            raise ValueError('Index should be less than the length of the linked list')

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.previous = new_node
            self.head = new_node
            if self.length == 0:
                self.tail = new_node
        elif index == self.length:
            new_node.previous = self.tail
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
        else:
            node_at_previous_index = self._get_node(index - 1)
            node_at_current_index = node_at_previous_index.next

            new_node.next = node_at_current_index
            new_node.previous = node_at_previous_index

            node_at_previous_index.next = new_node

            if node_at_current_index:
                node_at_current_index.previous = new_node

        self.length += 1
        print(self)

    def remove(self, index: int):
        """
        Remove the node at the given index from the linked list.

        This method updates the connections within the list to exclude the node at the specified index.
        Special cases are handled for removing the head or the tail of the list.

        Args:
            index (int): The index of the node to be removed.

        Raises:
            ValueError: If the index is not a non-negative integer or if it is out of the bounds of the linked list.
        """
        if not isinstance(index, int):
            raise TypeError('The index must be an integer')

        if index >= self.length or index < 0:
            raise ValueError('Index should be less than or equal to the length of the linked list and it should be non-negative')

        if index == 0:
            if self.length == 1:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
                self.head.previous = None

        else:
            node_at_previous_index = self._get_node(index - 1)
            node_to_remove = node_at_previous_index.next

            if node_to_remove.next:
                node_to_remove.next.previous = node_at_previous_index

            node_at_previous_index.next = node_to_remove.next

            if index == self.length - 1:
                self.tail = node_at_previous_index

        self.length -= 1
        print(self)

    def get(self, index: int) -> Any:
        """
        Get the value of the node at the given index in the linked list.

        Args:
            index (int): The index of the node whose value is to be retrieved.

        Returns:
            Any: The value of the node at the given index.

        Raises:
            TypeError: If the index is not an integer.
            ValueError: If the index is out of the bounds of the linked list.
        """
        if not isinstance(index, int) or index < 0:
            raise TypeError('The index must be a non-negative integer')

        if index >= self.length:
            raise ValueError('Index should be less than the length of the linked list')

        node = self._get_node(index)
        return node.value

    def _get_node(self, index: int) -> Node:
        """
        Get the node at the given index in the doubly linked list.

        This method optimizes the traversal by starting from the head or the tail,
        depending on which is closer to the given index.

        Args:
            index (int): The index of the node to be retrieved.

        Returns:
            Node: The node at the given index.
        """
        if index < self.length // 2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length - 1, index, -1):
                node = node.previous
        return node

