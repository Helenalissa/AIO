class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, value):
        if self.is_full():
            raise Exception("Stack is full")
         
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

stack1 = MyStack(5)

stack1.push(1)
stack1.push(2)

print(stack1.is_full())  # Output: False
print(stack1.top())  # Output: 2

print(stack1.pop())  # Output: 2
print(stack1.top())  # Output: 1

print(stack1.pop())  # Output: 1
print(stack1.is_empty())  # Output: True