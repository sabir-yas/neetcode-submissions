from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):

                if(board[i][j] == "."):
                    continue
                if(board[i][j] in rows[i]):
                    return False
                if(board[i][j] in cols[j]):
                    return False
                if(board[i][j] in squares[(i//3),(j//3)]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[i//3, j//3].add(board[i][j])

        return True

''''
we have defaultdict sets. to see if we have any duplicates
check duplicates in rows, check duplicates in columns and check duplicates in the 3/3 block
for i in range(9)
for j in range(9)
    check board array-given
    if it's ".", continue
    if it's in row set, return false
    if it's in column set, return false
    if it's in 3/3 set, r//3 c//3, return false

    row[i].add(board[i][j])
    cols[j].add(board[i][j])
    squares[r//3, c//3].add(board[i][j])


'''