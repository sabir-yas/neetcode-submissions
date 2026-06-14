class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first = strs[0]
        ind =0
        res=""

        for i in strs[0]:

            for j in range(1,len(strs)):
                if ind >= len(strs[j]) or i != strs[j][ind]:
                    return res
            ind+=1
            res+=i
                
        
        return res


