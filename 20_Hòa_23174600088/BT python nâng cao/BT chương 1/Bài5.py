class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def count(self):
        return len(self.items)
    

my_stack = Stack()


my_stack.push(1)
my_stack.push(2)
my_stack.push(3)


print(my_stack.count()) 