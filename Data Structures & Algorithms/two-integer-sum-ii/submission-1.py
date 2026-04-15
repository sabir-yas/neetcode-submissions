class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        hashMap = {}

        for i,n  in enumerate(numbers):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff]+1, i+1 ]
            hashMap[n]= i
        problem with this: space complexity of O(n)
        We can reduce this to O(1)
        '''

        l = 0
        r = len(numbers) - 1

        while( l < r):
            curSum = numbers[l] + numbers[r]
            if(curSum > target):
                r-=1
            elif(curSum < target):
                l+=1
            else:
                return [l+1, r+1]
        