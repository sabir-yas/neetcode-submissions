class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s) 
        s = "".join(s)

        t = sorted(t) 
        t = "".join(t)
        return s== t

