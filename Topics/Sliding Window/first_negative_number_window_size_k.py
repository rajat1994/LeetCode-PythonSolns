from collections import deque
z = 3
l = [12,-1,-7,12,-13,90]
q = deque()
k =[]


i = 0
j = 0

while j<len(l):
    if l[j] < 0:
        q.appendleft(l[j])

    if j-i+1<z:
        j+=1

    elif j-i+1 == z:
        if len(q) == 0:
            k.append(0)

        else:
           k.append(q[-1])
           if l[i] == q[-1]:
             q.pop()

        i+=1
        j+=1


print(k)





