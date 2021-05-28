from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)
stack.append(7)

k = len(stack)//2 +1

def del_middle (stack,k):
    if k ==1  :
        stack.pop()
        return

    x = stack.pop()
    del_middle(stack,k-1)
    stack.append(x)


del_middle(stack,k)
print(stack)

