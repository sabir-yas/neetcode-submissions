class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        #brute force
        maxcount = 0
        
        for i in range(len(s)):
            seen = set()
            currcount = 0
            
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    currcount += 1
                    maxcount = max(maxcount, currcount)
                else:
                    break
                    
        return maxcount
        '''

        #optimal- sliding window, O(n) time and O(n) space

        charSet = set()
        l = 0
        res =0

        for r in range(len(s)):
            #if duplicate found
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l + 1)
        
        return res










