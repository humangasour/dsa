class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.__dict__)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get_node_at_index(self, index):
        if index >= self.length:
            return self.tail

        node = self.head
        for i in range(index):
            node = node.next
        return node

    def insert(self, index, data):
        if index >= self.length:
            return self.append(data)

        if index == 0:
            return self.prepend(data)

        new_node = Node(data)
        preceding_node = self.get_node_at_index(index - 1)
        new_node.next = preceding_node.next
        preceding_node.next = new_node
        self.length += 1

    def remove(self, index):
        if index >= self.length:
            return None

        if index == 0:
            self.head = self.head.next
        else:
            preceding_node = self.get_node_at_index(index - 1)
            node_to_be_removed = preceding_node.next
            preceding_node.next = node_to_be_removed.next
        self.length -= 1

    def reverse(self):
        if self.length == 1:
            return self.head

        self.tail = self.head
        current_node = self.head
        next_node = self.head.next
        while next_node:
            temp = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = temp
        self.head.next = None
        self.head = current_node

    def print_list(self):
        if self.head is None:
            print('Empty')
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=' ')
                current_node = current_node.next
        print('\n')

