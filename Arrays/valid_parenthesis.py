class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()
        
        d1 = {'{':0, '(':1,'[':2}
        d2 = {'}':0, ')':1,']':2}
        
        
        for i in s:
            if i in ['{','(', '[']:
                stack.append(i)
                
            else :
                if len(stack) !=0 and  d2[i] == d1[stack[-1]]:
                    stack.pop()
                    
                else:
                    return False
                    
        if len(stack) == 0:
            return True
        
        else:
            False
        