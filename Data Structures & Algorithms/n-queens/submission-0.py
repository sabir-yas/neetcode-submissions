class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res=[]

        cols = set()
        posDiag= set() # (r+c)
        negDiag= set() # (r-c)

        board = [["."] * n for i in range(n)] # . .

        def backtrack(r):
            
            if r == n:
                res.append(["".join(row) for row in board]) # make sure to append each row,make sure to add list
                return
            
            for c in range(n): #in range n
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                board[r][c] = "Q" # make sure to add the queen, since the conditions are satisfied
                backtrack(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res