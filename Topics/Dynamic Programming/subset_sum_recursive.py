l = [1,908,101]

sum = 1009
n = len(l)



def subset_sum_recursive (l,sum,n):
    
    if sum == 0:
        return True

    if n == 0:
        return False

    if l[n-1]<=sum:
          return subset_sum_recursive(l,sum-l[n-1],n-1) or subset_sum_recursive(l,sum,n-1)
          

    return subset_sum_recursive(l,sum,n-1)


print(subset_sum_recursive(l,sum,n))






    

    