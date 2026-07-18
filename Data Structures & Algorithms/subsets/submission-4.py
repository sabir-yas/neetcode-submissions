class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [] #entire list of subset

        subset = [] #current subset

        def dfs(i):

            if i == len(nums):
                res.append(subset.copy())
                return
            
            #choose to add the number
            subset.append(nums[i])
            dfs(i+1)

            #choose to not add the number
            subset.pop()
            dfs(i+1)

            return res


        dfs(0) #pass the index
        return res