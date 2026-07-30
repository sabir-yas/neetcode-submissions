class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        res = [-s for s in stones]
        heapq.heapify(res)

        while len(res) > 1:
            first = heapq.heappop(res) #-8
            second = heapq.heappop(res) #-3

            #don't have to do anything if both are the same, just pop them
            if( second > first):
                heapq.heappush(res, first - second)
        
        #edge case
        res.append(0)
        return abs(res[0])

