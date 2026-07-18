class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        if len(nums) ==0:
            return [[]]

        trace = self.permute(nums[1:])

        for p in trace:
            for i in range(len(p) + 1):
                p_copy = p.copy() #either one number or array
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res