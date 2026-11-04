class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        # -4, -1, -1, 0, 1, 2
        res =[]
        for i, num in enumerate(nums):

            if i > 0 and nums[i-1] == num:
                continue

            l, r = i+1, len(nums)-1 # should be i+1
            while l < r:
                if num + nums[l] + nums[r] == 0:
                    res.append( [num, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l]== nums[l-1]:
                        l+=1

                elif num + nums[l] + nums[r] > 0:
                    r-=1

                elif num + nums[l] + nums[r] < 0:
                    l+=1
                
        return res        
            
        