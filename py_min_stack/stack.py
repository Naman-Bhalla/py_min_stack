class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        if not self.stack:
            self.stack.append((item, 0))
        else:
            smallest_index = self.stack[-1][-1]
            if item < self.stack[smallest_index][0]:
                smallest_index = len(self.stack)
            self.stack.append(item, smallest_index)

    def pop(self):
        if self.stack:
            return self.stack.pop()[0]
        else:
            raise IndexError

    def find_min(self):
        if self.stack:
            return self.stack[self.stack[-1][1]][0]
        else:
            raise IndexError

    def peek(self):
        if self.stack:
            return self.stack[-1][0]
        else:
            raise IndexError

    def __len__(self):
        return len(self.stack)
