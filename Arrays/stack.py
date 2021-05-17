from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,data):
        return self.container.append(data)

    def peek(self):
        return self.container[-1]

    def pop(self):
        return self.container.pop()

    def isempty(self):
        return len(self.container) == 0

    def length(self):
        return len(self.container)


S = Stack()

S.push(4)
S.push(10)
S.push(11)

print(S.length())
print(S.peek())
print(S.pop())
print(S.length())
print(S.isempty())