class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # O(n) time and space approach

        q = collections.deque() # store indexes, monotonically decreasing
        l=r=0
        output=[]

        while r < len(nums):
            #keep adding until get greater value, then start popping
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #popleft if element in queue is outside window
            if l > q[0]:
                q.popleft()

            #addmax value in window to output array
            if (r+1) >=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        
        return output