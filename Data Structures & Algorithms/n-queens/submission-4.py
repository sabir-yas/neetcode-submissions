class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        posDiag = set() #r +c
        negDiag = set() #r -c

        board = [["."] * n for i in range(n)]

        res = []

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board] # not board[row], since row is the actual row here
                res.append(copy)
                return
            
            # don't need this f (r < 0 or c < 0 or r > len(board) or c > len(board[0])
          
            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                board[r][c] = "Q"
                
                dfs(r+1) # got to increment row

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

                board[r][c] = "."

        dfs(0)
        return res

        
            
            


