l = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4

sum = 0
max_sum = 0

i = 0
j = 0

while j<len(l) :    
    sum = sum + l[j]
    
    if ((j-i)+1) < k:
        j = j+1

    elif ((j-i)+1) == k:
        
        max_sum = max(sum,max_sum)
        sum = (sum - l[i])
        i+=1
        j+=1


print(max_sum)

    





