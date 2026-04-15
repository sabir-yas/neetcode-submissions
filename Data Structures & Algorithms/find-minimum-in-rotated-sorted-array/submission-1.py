class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        #use binary search, get middle element, check if it is smaller than 1st element, if
        #yes, then 

        l, r = 0, len(nums) -1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
                
        return res

            