from common.node_class import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        if self.length == 0:
            return 'Empty Queue'

        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            print('Empty Queue')
        else:
            self.first = self.first.next
            self.length -= 1
            if self.length == 0:
                self.last = None

    def print_queue(self):
        if self.length == 0:
            print('Empty Queue')
        else:
            current_node = self.first
            while current_node is not None:
                print(current_node.value, end=' ')
                current_node = current_node.next
            print('\n')
