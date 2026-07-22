class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "qprs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i, curStr): # i->tell which digit we are at in digits string, curStr- what string we're at

            #base case
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in digitToChar[digits[i]]: # every letter in say, 2:- then a, b , and c
                backtrack(i+1, curStr + c)
        
        if digits: # only if digits is non-empty, don't want [""], only want []
            backtrack(0, "")
        return res
