class Stack:
    def __init__(self):
        self.stack = []
        self.current_minimum = float('inf')

    def push(self, item):
        if not self.stack:
            self.stack.append(item)
            self.current_minimum = item
        else:
            if item >= self.current_minimum:
                self.stack.append(item)
            else:
                self.stack.append(2 * item - self.current_minimum)
                self.current_minimum = item

    def pop(self):
        if not self.stack:
            raise IndexError
        else:
            item = self.stack.pop()
            if item >= self.current_minimum:
                return item
            else:
                answer = self.current_minimum
                self.current_minimum = 2 * self.current_minimum - item
                return answer

    def peek(self):
        if not self.stack:
            raise IndexError
        else:
            item = self.stack[-1]
            if item >= self.current_minimum:
                return item
            else:
                return self.current_minimum

    def find_min(self):
        if not self.stack:
            return IndexError
        return self.current_minimum

    def __len__(self):
        return len(self.stack)