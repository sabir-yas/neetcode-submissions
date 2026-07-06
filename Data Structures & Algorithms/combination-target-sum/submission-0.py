class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res= []

        def dfs(i, cur, total): #index, current combo, and the total sum

            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            #choose to add a number
            cur.append(nums[i])
            dfs(i, cur, total+nums[i])

            #choose to not add a number
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)

        return res