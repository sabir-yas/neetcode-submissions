class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #optimal solution, let's do this in one pass two times
        '''
        first pass(left to right)
        second pass(right to left)

        time - O(n), space - O(1) extra space and O(n) space for output array

        '''

        arr = [1] * len(nums)

        prefix =1
        for i in range(len(nums)):
            arr[i] = prefix # first say the index equals prefix, then multiply prefix *= nums[i]
            prefix *= nums[i]

        postfix =1
        for j in range(len(nums)-1, -1, -1):
            arr[j] *= postfix
            postfix *= nums[j]
        
        return arr
