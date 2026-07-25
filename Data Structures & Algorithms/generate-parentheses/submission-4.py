class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        # openN < closeN
        # openN > closeN
        # openN == closeN
        
        def backtrack(openN, closeN, curStr): # openN and closeN are the number of brackets
            
            if openN == closeN == n :
                res.append(curStr)
                return

            if openN < n:
                backtrack(openN +1, closeN, curStr +"(")
                
            if openN > closeN:
                backtrack(openN, closeN+ 1, curStr + ")")
            

        backtrack(0,0, "")
        return res


      






















            