class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        '''
        Time complexity: O(m*n)
        Space complexity: O(m*n) extra space
        arr = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                arr.append(matrix[i][j])
        
        #binary search
        l = 0
        r = len(arr) -1

        while l <= r:
            mid = (l+r) //2
            if arr[mid] < target:
                l = mid+1
            elif arr[mid] > target:
                r = mid-1
            else:
                return True
        
        return False

        '''
        
        #Time complexity: O(log m * n)
        #Space complexity: O(1)

        #two binary search
        #a loop that finds which of the individual rows the value is in 
        #a loop that find where in these individual cols of this row the value exactly is

        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS -1
        while top <= bot:
            row = (top + bot) //2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        l, r = 0, COLS -1

        row = (top+bot)//2
        while l <=r:   
            mid = (l + r)//2
            if matrix[row][mid] > target:
                r = mid -1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False

        

            
