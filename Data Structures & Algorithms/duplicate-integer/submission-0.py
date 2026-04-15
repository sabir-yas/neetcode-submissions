class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Set = set()

        for i in nums: 
            if i in Set:
                return True
            Set.add(i)

        return False