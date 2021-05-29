class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = {}

        for i in range(len(s)):
           if s[i] in d:
            d[s[i]] = ''
            
           else :
            d[s[i]] = i
        
        for i in d.keys():
            if d[i] != '':
                return d[i]
            
        return -1