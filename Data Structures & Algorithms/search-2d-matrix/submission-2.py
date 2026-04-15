class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
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
