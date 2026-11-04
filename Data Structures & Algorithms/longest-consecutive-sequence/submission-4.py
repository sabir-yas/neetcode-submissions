class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashSet = set(nums)
        count = 0
        maxCount =0

        for i in hashSet:
            if (i -1) not in hashSet:
                length = 0

                while i+length in hashSet:
                    length+=1
                maxCount = max(maxCount, length)
                
        return maxCount

