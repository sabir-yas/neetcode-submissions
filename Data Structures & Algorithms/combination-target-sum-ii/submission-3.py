class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        candidates.sort() #remember to sort
        def dfs(i, cur, total): #backtrack
            if total == target:
                res.append(cur.copy())
                return

            if i == len(candidates) or total > target:
                return

            #include candidates[i]
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i]) #cannot use the current number again
            cur.pop()

            #skip candidates[i]

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i+=1
            dfs(i+1, cur, total)

            return res

        dfs(0, [], 0)
        return res