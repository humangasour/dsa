import json
from typing import Union


class Node:
    def __init__(self, value: int):
        self.right = None
        self.left = None
        self.value = value

    def __str__(self):
        return str(self.__dict__)

    def to_json(self):
        return json.dumps(
                self,
                default=lambda o: o.__dict__, sort_keys=True, indent=4
        )


class BinarySearchTree:
    def __init__(self):
        self.root: Union[Node, None] = None

    def to_json(self):
        return json.dumps(
                self,
                default=lambda o: o.__dict__, sort_keys=True, indent=4
        )

    def insert(self, value: int):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if current_node.value == new_node.value:
                    print('No duplicate values allowed')
                    break
                if current_node.value < new_node.value:
                    # traverse on the RIGHT side of the node
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        break
                else:
                    # traverse on the LEFT side of the node
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        break

    def lookup(self, value: int) -> Union[Node, None]:
        if self.root is None:
            print('Binary Tree Empty')
            return
        else:
            current_node = self.root
            while current_node is not None:
                if current_node.value == value:
                    return current_node
                elif current_node.value < value:
                    current_node = current_node.right
                else:
                    current_node = current_node.left
            print(f'Value: {value} does not exist in tree')

    def remove(self, value: int):
        if self.root is None:
            print('Binary Tree Empty')
            return
        else:
            current_node = self.root
            parent_node = None
            while True:
                # usual traversal
                if current_node is None:
                    print('Value does not exist in tree')
                    return
                elif current_node.value < value:
                    parent_node = current_node
                    current_node = current_node.right
                    continue
                elif current_node.value > value:
                    parent_node = current_node
                    current_node = current_node.left
                    continue
                elif current_node.value == value:
                    # we've found the target node, let's get to work now
                    if current_node.right is None:  # no right child
                        if parent_node is None:  # if root
                            self.root = current_node.left
                        else:
                            if current_node.value < parent_node.value:
                                parent_node.left = current_node.left
                            elif current_node.value > parent_node.value:
                                parent_node.right = current_node.left
                    elif current_node.right.left is None:  # if there is a right child which does not have a left child
                        if parent_node is None:  # if root
                            self.root = current_node.left
                        else:
                            current_node.right.left = current_node.left

                            if parent_node.value > current_node.value:
                                parent_node.left = current_node.right
                            elif parent_node.value < current_node.value:
                                parent_node.right = current_node.right
                    else:  # if there is right child which has a left child
                        # find the left most node
                        left_most_node = current_node.right.left
                        left_most_parent_node = current_node.right
                        while left_most_node.left is not None:
                            left_most_parent_node = left_most_node
                            left_most_node = left_most_node.left

                        left_most_parent_node.left = left_most_node.right
                        left_most_node.left = current_node.left
                        left_most_node.right = current_node.right

                        if parent_node is None:
                            self.root = left_most_node
                        else:
                            if current_node.value < parent_node.value:
                                parent_node.left = left_most_node
                            elif current_node.value > parent_node.value:
                                parent_node.right = left_most_node
                    break
            return True
