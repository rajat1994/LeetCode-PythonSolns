

k = 0
def no_of_parenthesis (op,o,c):
        
        if o == 0 and c ==0:
            print(op)
            return


        if o !=0:
            op1 = op
            op1 = op1+"("
            no_of_parenthesis (op1,o-1,c)


        
        
            
        if c>o:
            
            op1 = op
            op1 = op1 + ")"
            no_of_parenthesis (op1,o,c-1)
            
        
            
        
        
    
    
no_of_parenthesis("",4,4)
        
        