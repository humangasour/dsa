class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.__dict__)


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        if self.length == 0:
            return 'Empty Stack'

        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            self.top.next = new_node
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            print('Empty Stack')
        else:
            second_last_node = self.bottom
            for i in range(1, self.length - 1):
                second_last_node = second_last_node.next
            last_node = second_last_node.next
            second_last_node.next = None
            self.top = second_last_node
            self.length -= 1
            if self.length == 0:
                self.bottom = None
            return last_node

    def print_stack(self):
        if self.length == 0:
            print('Empty Stack')
        else:
            current_node = self.bottom
            while current_node is not None:
                print(current_node.value, end=' ')
                current_node = current_node.next
            print('\n')
