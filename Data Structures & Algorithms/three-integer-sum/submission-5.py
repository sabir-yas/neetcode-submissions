class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        '''
        brute force- have errors in this, has problems in duplicate detection, has set.
        arr = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if k != j and k != i:
                        if(nums[i]+nums[j]+nums[k]) == 0 and [nums[i], nums[j], nums[k]] not in arr:
                            arr.append([nums[i], nums[j], nums[k]])
        return arr

        neet's style of this-> note he adds to the set by adding a tuple, and returns 
                                                            [list(i) for i in res]
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if(nums[i]+nums[j]+nums[k]) == 0
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]
        '''
        arr = []
        nums.sort()

        #trying 2 pointer approach
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l= i+1
            r= len(nums) - 1
            
            while(l < r):
               # if nums[l] + nums[r] == (nums[i]*-1):
               #     arr.append([nums[i], nums[l], nums[r]]) this is my code- correct logic
                Sum = nums[i] + nums[l] + nums[r]
                if Sum > 0:
                    r -=1
                elif Sum < 0:
                    l +=1
                else:
                    arr.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                #l+=1 
                #r-=1 my previous additions
        return arr



                    