def permutation_with_case_change (ip,op):


    if  ip == "":
        print(op)
        return


    op1 = op
    op2 = op

    op1 = op1 + ip[0]
    op2 = op2 +  ip[0].upper()
    
    ip  = ip[1:]

    permutation_with_case_change(ip,op1)
    permutation_with_case_change(ip,op2)



permutation_with_case_change("ab", "")
