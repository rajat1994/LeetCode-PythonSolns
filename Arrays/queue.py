from collections import deque
class Queue:
    def __init__ (self):
        self.buffer = deque()

    def enqueue(self,data):
        return self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()

    def isempty(self):
        return len(self.buffer) == 0

    def length(self):
        return len(self.buffer)


Q = Queue()

Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(6)

print(Q.length())

print(Q.dequeue())

print(Q.length())

print(Q.isempty())