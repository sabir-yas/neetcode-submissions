class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #check if lengths are the same
            return False
        
        countS, countT = {}, {} # create hashmaps

        for i in range(len(s)): # create a for loop, count the frequency of each letter in the hashmap
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for i in countS: #loop through the hashmap, check if frequency of letter in first hashmap is equal to 2nd hashmap. 
            if countS[i] != countT.get(i, 0):
                return False
        return True

'''
        if len(s) != len(t):
            return

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS.get(c) != countT.get(c, 0):
                return False
        return True
'''



'''
        brute force
        s = sorted(s) 
        s = "".join(s)

        t = sorted(t) 
        t = "".join(t)
        return s== t

'''


















