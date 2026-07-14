class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        #recursion
        if len(nums) ==0:
            return [[]]

        permute =  self.permute(nums[1:])# recursively making nums smaller
        res=[]
        for p in permute:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res

