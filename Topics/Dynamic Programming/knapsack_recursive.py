wt = [2,3,4,7,5]
val = [1,3,4,6,7]
W = 12
n = len(wt)


def knapsack_recursive(val,wt, W, n):

    if n == 0 or W == 0:
        return 0

    elif wt[n-1]<=W:
        return max( val[n-1] + knapsack_recursive(val,wt, W-wt[n-1],n-1), knapsack_recursive(val,wt,W,n-1))

    elif wt[n-1] > W:
        return knapsack_recursive(val,wt,W,n-1)


print(knapsack_recursive(val,wt,W,n))

    