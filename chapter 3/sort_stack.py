class SortStack:
    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def push(self, value):
        self.stack.append(value)
        self.sort()

    def pop(self):
        return self.stack.pop()

    def sort(self):
        while self.stack:
            temp = self.stack.pop()
            while self.temp_stack and self.temp_stack[-1] < temp:
                self.stack.append(self.temp_stack.pop())
            self.temp_stack.append(temp)
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())

    def __str__(self):
        return str(self.stack)