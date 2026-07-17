class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count={}
        l = 0
        res = 0
        maxf = 0

        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -=1
                l+=1
            
            res = max(res, r - l +1)
        
        return res

        


        ''' 
        test with comments
        l= 0
        res=0
        charMap=defaultdict(int)
        maxf=0

        for r in range(len(s)):

            #count frequency
            charMap[s[r]] +=1
            maxf= max(maxf,charMap[s[r]])

            #check if valid in window
            while (r-l+1) - maxf > k:
                charMap[s[l]]-=1
                l+=1
            #check max window size
            res= max(res, (r-l+1))
        
        return res
        '''

        #brute force
        '''

        res = 0
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res
        '''
    

























