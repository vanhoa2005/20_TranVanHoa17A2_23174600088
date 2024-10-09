class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.top = -1
        self.array = [0.0] * max_size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, item):
        if self.is_full():
            print("Stack overflow")
            return
        self.top += 1
        self.array[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return
        item = self.array[self.top]
        self.top -= 1
        return item
    

stack = Stack(5)

stack.push(2.5)
stack.push(3.14)
stack.push(1.618)

item = stack.pop()
print(item)  # In ra: 1.618