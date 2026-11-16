class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]

        l, r =0, len(nums) - 1


        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                # not return nums[l]

            mid = (l+r)//2
            res = min(res, nums[mid]) # we find it here

            if nums[mid] >= nums[l]:
                l = mid+1
                # not res = min(res, nums[l])

            else:
                r = mid-1
                # not res = min(res, nums[r])
            
        return res

            