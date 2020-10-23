# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# Brayden Brown

class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    
    def pop(self):
        if self.is_empty():
            raise IndexError
        else:
            return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError
        else:
            return self.data[-1]

    def push(self, value):
        self.data.append(value)

    pass
