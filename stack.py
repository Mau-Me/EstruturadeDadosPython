class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]
    
    def sizeStack(self):
        return len(self.stack)

#Example#

stack = Stack()

stack.push(5)
stack.push(7)
stack.push(3)

print(stack.stack.pop())


for i in range(stack.sizeStack()):
    print(stack.pop())

print(stack.sizeStack())