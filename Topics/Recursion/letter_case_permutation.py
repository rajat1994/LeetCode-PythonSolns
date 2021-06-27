

l = ["1", "2"]

def permutation_with_case_change (ip,op):


    if  ip == "":
        print(op)
        return

    if ip[0] not in l:
     op1 = op
     op2 = op
    
     op1 = op1 + ip[0].lower()
     op2 = op2 +  ip[0].upper()

     ip  = ip[1:]

     permutation_with_case_change(ip,op1)
     permutation_with_case_change(ip,op2)
    

    else :

     op1 = op
     op1 = op1 + ip[0]
     ip  = ip[1:]
     permutation_with_case_change(ip,op1)


    
    



permutation_with_case_change("a1B2", "")
