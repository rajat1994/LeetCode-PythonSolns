def print_one_to_n(n):

    if n == 1:
        print(1)
        return

    print_one_to_n(n-1)
    print(n)



print_one_to_n(5)