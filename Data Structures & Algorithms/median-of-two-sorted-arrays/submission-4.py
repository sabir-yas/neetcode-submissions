class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #brute force- O((m+n)log(m+n)) time, and  O(m + n) extra space
        #remember median, if n is odd(3 or greater odd)->middle element, if n is even middle 2 elements
        '''
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
        '''

        #binary approach to cut down time to O(log(min(n,m))) time and O(1) space, where n is the size
        #of nums1 and m is the size of nums2


        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A)-1

        while True:
            i = (l+r) // 2
            j = half - i - 2 # -2 is to offset off by one- remember i is index, j is index, half is length

            Aleft = A[i] if i >= 0 else float("-infinity") 
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright: #found the right partition
                if total %2 !=0:
                    #odd
                    return min(Aright, Bright)
                else:
                    #even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) /2
            elif Aleft > Bright:
                r = i -1
            else:
                l = i + 1
            

        