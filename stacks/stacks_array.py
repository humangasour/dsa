class Stack:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.array[len(self.array) - 1]

    def pop(self):
        if len(self.array) != 0:
            return self.array.pop()
        else:
            print('Stack Empty')
            return

    def push(self, value):
        return self.array.append(value)

    def print_stack(self):
        for i in range(len(self.array) - 1, -1, -1):
            print(self.array[i])
        return
