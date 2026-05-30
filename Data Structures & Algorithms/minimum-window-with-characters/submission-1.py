class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        #s = "OUZODYXAZV", t = "XYZ"
        
        if t == "":
            return ""
        
        tCount={}
        window={}

        for i in t:
            tCount[i] = 1+ tCount.get(i,0)
        
        have, need= 0, len(tCount)

        l=0
        res, resLen= [-1,-1], float("infinity")

        for r in range(len(s)):
            c= s[r]
            window[c] = 1 + window.get(c, 0)

            if c in tCount and tCount[c] == window[c]:
                have+=1
            
            while have == need:
                #find new min res
                if(r-l+1) < resLen:
                    res=[l,r]
                    resLen=(r-l+1)
                
                #shrink window
                window[s[l]]-=1 # since decremented-possible have != need.
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else "" # take note of off by one error and return string
        
        









                
            


