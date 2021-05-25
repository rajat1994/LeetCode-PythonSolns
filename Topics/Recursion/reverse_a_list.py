

l = [1,2,4,5]


def reverse(l):
    if len(l) ==1:
        return

    x = l.pop()
    
    reverse(l)
    l.insert(0,x)



reverse(l)
print(l)
    

