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

        total = len(nums1) + len(nums2)      # total number of elements in both arrays
        half = total // 2                    # number of elements we want on the left side

        A, B = nums1, nums2                  # A is the array we binary search on

        if len(B) < len(A):                  # make sure A is the smaller array
            A, B = B, A                      # swap so binary search is faster/safer

        l, r = 0, len(A) - 1                 # binary search boundaries for A

        while True:                          # keep searching until correct partition is found
            i = (l + r) // 2                 # i = last index on left side of A
            j = half - i - 2                 # j = last index on left side of B

            Aleft = A[i] if i >= 0 else float("-inf")          # value left of A cut, or -inf if empty
            Aright = A[i + 1] if i + 1 < len(A) else float("inf") # value right of A cut, or inf if empty

            Bleft = B[j] if j >= 0 else float("-inf")          # value left of B cut, or -inf if empty
            Bright = B[j + 1] if j + 1 < len(B) else float("inf") # value right of B cut, or inf if empty

            if Aleft <= Bright and Bleft <= Aright:  # correct partition: all left values <= all right values
                if total % 2 != 0:                   # odd total length
                    return min(Aright, Bright)       # median is the smallest value on the right side
                else:                                # even total length
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                                                    # median is avg of largest left + smallest right

            elif Aleft > Bright:                     # A's left value is too big
                r = i - 1                            # move A partition left

            else:                                    # Bleft > Aright, so A's partition is too far left
                l = i + 1                            # move A partition right
            

 #  B= [1,2,3,5,6,7,8]
 #  A= [1,2,3,4]   
































        