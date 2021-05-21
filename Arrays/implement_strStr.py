class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if haystack == needle:
            return 0
        
        
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        
        i = 0
        
        while i < len(haystack):
               if haystack[i:i+len(needle)] == needle:
                  return i
            
            
               i = i+1 
        
        return -1
        