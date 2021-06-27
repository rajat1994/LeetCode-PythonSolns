
def subsets (ip, op):
    if len(ip) == 0:
        print(op)
        return

    op1 = op
    op2 = op

    op2 = op2+ip[0]
    ip = ip[1:]

    subsets(ip,op1)
    subsets(ip,op2)


subsets("abc","")

