class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        res= [ -s for s in stones]
        heapq.heapify(res)

        while len(res) > 1:
            first = heapq.heappop(res) #=8
            second = heapq.heappop(res) #=7

            if second > first:
                heapq.heappush(res, first- second) #second - first( -7+8= -1), but first - second(-8+7=-1)
        
        res.append(0)
        return abs(res[0])