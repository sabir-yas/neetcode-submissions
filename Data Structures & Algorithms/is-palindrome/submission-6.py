class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # idea is to have two pointers
        # one going from left another from right
        # time complexity of this is O(n) and O(1)

        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        
        return True

        '''
        brute force- reverse string
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        '''
