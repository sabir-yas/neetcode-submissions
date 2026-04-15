class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Set = set()

        for i in range(len(nums)):
            if nums[i] in Set:
                return True
            Set.add(nums[i])
        return False
        
        '''
        '''
        Set = set()

        for i in nums: 
            if i in Set:
                return True
            Set.add(i)

        return False
        '''

        Set = set()

        for i in nums:
            if i in Set:
                return True
            Set.add(i)
        return False

        