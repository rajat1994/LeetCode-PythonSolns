from collections import deque

stack = deque()

stack.append(5)
stack.append(1)
stack.append(0)
stack.append(2)


def sort(stack):

    if len(stack) == 0:
        return

    x = stack.pop()
    sort(stack)
    insert(stack,x)

def insert(stack,x):

    if len(stack) == 0 or stack[-1] <= x:
        stack.append(x)
        return

    temp = stack.pop()
    insert(stack,x)
    stack.append(temp)


print(stack)

sort(stack)

print(stack)
