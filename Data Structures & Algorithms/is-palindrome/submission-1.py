class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        res = ""

        for i in s:
            if ((ord(i) >= ord ("a") and ord(i) <= ord("z")) or 
                (ord(i) >= ord("A") and ord(i) <= ord("Z")) or
                (ord(i) >= ord('0') and ord(i) <= ord('9'))):
                res += i
        
        res = res.lower()

        return res == res[::-1]
        '''  

        #isalnum
        '''
        newStr = "" extra memory here
        for c in s:
            if c.isalnum():
                newStr+= c.lower()
        newStr == newStr[::-1] extra memory here

        '''
        #using o(1) memory
        #going to have two pointers
        l, r = 0, len(s)-1

        while l < r:
            while(l < r and not self.alphaNum(s[l])):
                l+=1
            while(r > l and not self.alphaNum(s[r])):
                r-=1
            if(s[l].lower() != s[r].lower()):
                return False
            l= l+1
            r= r-1
        return True  

    def alphaNum(self, i):
        return i.isalnum()
