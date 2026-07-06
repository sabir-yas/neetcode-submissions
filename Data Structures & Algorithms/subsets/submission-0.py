class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res= [] #contain all subsets

        subset = [] #contains current subset

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            #choose to add a number
            subset.append(nums[i])
            dfs(i+1)

            #choose to not add a number
            subset.pop()
            dfs(i+1)

        dfs(0)

        return res