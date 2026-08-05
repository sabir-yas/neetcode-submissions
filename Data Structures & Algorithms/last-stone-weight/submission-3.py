class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        res = [-s for s in stones]
        heapq.heapify(res)

        while len(res) > 1:
            x = heapq.heappop(res)
            y = heapq.heappop(res)

            # x = -3, y = -8
            if x < y:
                heapq.heappush(res, x-y)

        #edge case- when s == 0
        res.append(0)
        return abs(res[0])