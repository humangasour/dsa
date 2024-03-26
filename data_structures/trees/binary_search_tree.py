from typing import Optional, List


class Node:
    """
    A node in a binary search tree.

    Attributes:
        key (int): The value stored in the node.
        left (Optional[Node]): A reference to the left child of the node, or None if the left child node is empty
        right (Optional[Node]): A reference to the right child of the node, or None if the right child node is empty
    """

    def __init__(self, key: int):
        """
        Initialize a Node with a given value.

        Args:
            key (Any): The value to be stored in the node.
        """
        self.key = key
        self.left = None
        self.right = None

    def __str__(self) -> str:
        """
        String representation of the node.

        Returns:
        str: A string representation of the node showing the key.
        """
        return str(self.key)


class BinarySearchTree:
    """
    A simple implementation of a binary search tree data structure.

    Attributes:
        root (Optional[Node]): A reference to the root node of the binary search tree, or None if the node is empty.
        size (int): The total number of nodes in the binary search tree.
    """

    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None
        self.size = 0

    def __str__(self):
        """
        String representation of the binary search tree.

        Returns:
        str: A string representing the binary search tree.
        """
        levels = []
        self._traverse_levels(self.root, 0, levels)
        return "\n".join(["Level {}: {}".format(level, ", ".join(nodes)) for level, nodes in enumerate(levels)])

    def _traverse_levels(
        self,
        node: Optional[Node],
        level: int,
        levels: List[List[str]]
    ) -> None:
        """
        Helper function to traverse the tree level by level.

        Args:
        node (Optional[Node]): The current node being traversed. Can be None.
        level (int): The current level in the tree.
        levels (List[List[str]]): A list containing lists of node keys, separated by tree levels.
        """
        if node is None:
            return
        if len(levels) == level:
            levels.append([])
        levels[level].append(str(node))
        self._traverse_levels(node.left, level + 1, levels)
        self._traverse_levels(node.right, level + 1, levels)

    def insert(self, key: int) -> bool:
        """
        Add a new node with the given value to the binary search tree.

        Args:
            key (int): The value to be stored in the node and added to the binary search tree.

        Returns:
            bool: True if the node was inserted, False if a node with the same key already exists.
        """
        if self.root is None:
            self.root = Node(key)
            self.size += 1
            return True

        target_node = self.root
        while True:
            if key > target_node.key:
                if target_node.right:
                    target_node = target_node.right
                else:
                    target_node.right = Node(key)
                    self.size += 1
                    return True
            elif key < target_node.key:
                if target_node.left:
                    target_node = target_node.left
                else:
                    target_node.left = Node(key)
                    self.size += 1
                    return True
            else:
                # Duplicate key, not inserting
                return False

    def Remove(self, key: int) -> bool:
        """
        Remove the node with the given key from the binary search tree.

        Args:
            key (int): The value of the node to be removed from the binary search tree.

        Returns:
            bool: True if the node was removed, False if the node does not exist in the binary tree.
        """
        parent_node = None
        current_node = self.root
        while current_node:
            if key > current_node.key:
                parent_node = current_node
                current_node = current_node.right
            elif key < current_node.key:
                parent_node = current_node
                current_node = current_node.left
            else:
                # Node with zero children (leaf)
                if not current_node.left and not current_node.right:
                    if parent_node:
                        if current_node.key > parent_node.key:
                            parent_node.right = None
                        else:
                            parent_node.left = None
                    else:
                        self.root = None

                # Node with one child
                elif current_node.left or current_node.right:
                    child = current_node.left if current_node.left else current_node.right
                    if parent_node:
                        if current_node.key > parent_node.key:
                            parent_node.right = child
                        else:
                            parent_node.left = child
                    else:
                        self.root = child

                # Node with two children
                else:
                    successors_parent_node = current_node
                    successor = current_node.right
                    while successor.left:
                        successors_parent_node = successor
                        successor = successor.left

                    if successors_parent_node != current_node:
                        successors_parent_node.left = successor.right
                    else:
                        successors_parent_node.right = successor.right

                    current_node.key = successor.key

                self.size -= 1
                return True

        return False  # Node not found

    def lookup(self, key: int) -> bool:
        """
        Checks if the value exists in the binary search tree.

        Args:
            key (int): The value to be searched in the binary search tree.

        Returns:
            bool: True if the value exists in the binary search tree, else False.
        """
        if self.size == 0:
            return False

        current_node = self.root
        while current_node:
            if key > current_node.key:
                current_node = current_node.right
            elif key < current_node.key:
                current_node = current_node.left
            else:
                return True
        return False
