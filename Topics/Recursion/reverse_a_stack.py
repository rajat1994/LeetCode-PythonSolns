from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)


def insert(stack, x):
    if len(stack) == 0:
        stack.append(x)
        return

    temp = stack.pop()
    insert(stack,x)
    stack.append(temp)

def reverse_stack (stack):
    if len(stack) == 1:
        return

    x = stack.pop()
    reverse_stack(stack)
    insert(stack,x)

print(stack)
reverse_stack(stack)
print(stack)


