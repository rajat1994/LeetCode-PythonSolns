l = [4,9,5]


def insert(l,x):

    if len(l)==0 or l[len(l)-1]<=x:
        l.append(x)
        return

    
    p = l.pop()
    insert(l,x)
    l.append(p)
        

    


def sort(l):
    if len(l) ==1:
        return 
    
    x = l.pop()
    sort(l)
    insert(l,x)

    


sort(l)
print(l)