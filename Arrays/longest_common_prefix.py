class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         
        min_length_string = min(len(s) for s in strs)
        
        res_string = ''
        curr_value = ''
        
        for i in range(min_length_string):
            curr_value = strs[0][i]
            
            for s in strs:
                if curr_value != s[i]:
                    return res_string
                
            res_string += curr_value
            
        return res_string