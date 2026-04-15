class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}

        count1 = [0] * 26
        count2 = [0] * 26

        for i in s:
            count1[ord(i)-ord("a")]+=1
        
        for j in t:
            count2[ord(j)-ord("a")]+=1

        if(count1==count2):
            return True

        return False
