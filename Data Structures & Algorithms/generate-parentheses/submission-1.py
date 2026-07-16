class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #recursive backtracking approach

        #add ( only if openN < n
        # add ) only if close < openN
        # valid only iff openN == close

        parens = []

        def backtrack(openN, close,arr):

            if openN == close == n:
                parens.append(arr)
                return 

            if openN < n:
                backtrack(openN+1,close, arr+ "(")
            
            if close < openN:
                backtrack(openN, close+1, arr+ ")")
            
        backtrack(0,0,"")

        return parens




















