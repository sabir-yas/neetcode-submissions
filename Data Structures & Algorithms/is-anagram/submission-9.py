class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        revMap = [0] * 26
        for i in s:
            revMap[ord(i) - ord("a")]+=1
        
        for j in t:
            revMap[ord(j) - ord("a")]-=1
        
        return revMap == [0] * 26
            