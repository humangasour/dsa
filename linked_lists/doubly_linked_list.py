class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.__dict__)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def append(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
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

        new_node = DoubleNode(data)
        preceding_node = self.get_node_at_index(index - 1)
        succeeding_node = preceding_node.next
        preceding_node.next = new_node
        new_node.next = succeeding_node
        new_node.prev = preceding_node
        succeeding_node.prev = new_node
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

    def print_list(self):
        if self.head is None:
            print('Empty')
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=' ')
                current_node = current_node.next
        print('\n')

