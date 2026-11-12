class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        '''
        binary search- kind of twice
        notice the start and end of each row
        '''

        ROWS = len(matrix)
        COLS = len(matrix[0])

        # two binary searches
        
        l, r = 0, ROWS-1

        while l <= r:
            mid = (l + r)//2
            
            if matrix[mid][0] > target:
                r = mid -1
            elif matrix[mid][COLS-1] < target:
                l = mid +1
            else:
                break
        else:
            return False

        ROW = (l+r)//2

        l, r =0, COLS -1 

        while l <= r:
            mid = (l+r)//2

            if matrix[ROW][mid] > target:
                r = mid-1
            elif matrix[ROW][mid] < target:
                l = mid+1
            else:
                return True

        return False
