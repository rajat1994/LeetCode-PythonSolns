
l = [1,2,3,4,5,34]


n = len(l)-1
def recursive_sum (l,n):
    if n == 0:
        return l[0]

    k = l[n]
    sum = recursive_sum(l,n-1) + k
    return sum
    


print(recursive_sum(l,n))

