class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #minheap with K largest integers

        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.minheap, val) # add the value
        #edge case what if we have less than k elements
        if len(self.minheap) > self.k: #pop the smallest value, 
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
