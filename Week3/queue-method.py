class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty") 
        return self.queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full") 
        self.queue.append(value)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")  
        return self.queue[0]

