class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #brute force
        #remember median, if n is odd(3 or greater odd)->middle element, if n is even middle 2 elements

        arr = []
        avr = 0.0

        for i in nums1:
            arr.append(i)
        for j in nums2:
            arr.append(j)
        
        arr.sort()

        if (len(nums1) + len(nums2)) % 2 != 0:
            l, r = 0, len(arr)-1
            mid = (l+r)//2
            return float(arr[mid])
        else:
            l, r = 0, len(arr) -1
            mid = (l+r)//2
            avr = (arr[mid]+ arr[mid+1]) / 2
        
        return avr


        