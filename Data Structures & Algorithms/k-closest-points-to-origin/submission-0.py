class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        for x, y in points:
            distance= math.sqrt( pow(x, 2) + pow(y, 2)) # don't need to take the sqrt
            res.append( [distance,x,y])
        
        heapq.heapify(res)
        ans = []
        while k > 0:
            dist, x, y = heapq.heappop(res)
            ans.append(([x, y]))
            k-=1
        
        return ans
            
        