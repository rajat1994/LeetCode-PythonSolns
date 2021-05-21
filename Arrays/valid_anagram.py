class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        d = defaultdict(lambda: 0)
        
        if len(s) != len(t):
            return False
            
            
        else:   
            
          i = 0
          while i< len(s):
                d[s[i]]+=1
                d[t[i]]-=1
                
                i = i+1
                
          for i in d.keys():
            if d[i] != 0:
                return False
            
          return True