class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #recursive backtracking approach

        #add ( only if open < n
        # add ) only if close < open
        # valid only iff open == close

        res = []
        stack = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
            
        backtrack(0,0)
        return res