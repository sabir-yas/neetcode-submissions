class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''
        just looking at the example- 3,4,5,6,1,2
        mid = 5, we just plainly look at the nums arr
        is nums[mid] > nums[l], this means we are in the left sorted section
            if yes- now check, is target greater than nums[mid]  or smaller than nums[l], then l = mid+1, else r= mid-1
        else: means we are in the right sorted section
            if target < nums[mid] or 
        '''

        #take 4,5,6,7,0,1,2 as an example-> 6-left sorted section and 1-right sorted section as the mids
        l, r = 0, len(nums)-1
        
        while( l<=r):
            mid = (l+r)//2
            
            if target == nums[mid]:
                return mid

            #mid is in left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:# target is greater than our mid, 
                                                        #than we know it has to be right of mid. 
                                                        #if target less than the leftmost element
                                                        #we know it has to be right of mid
                    l = mid +1
                else:
                    r = mid -1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                        l = mid + 1

        return -1