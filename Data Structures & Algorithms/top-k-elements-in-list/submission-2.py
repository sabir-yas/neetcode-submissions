from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute force- sort then get first k elements
        #most optimal - bucket sort algorithm
        '''
        count ={} #hashmap to sort count of each index
        freq = [[] for i in range(len(nums)+1)] #creating nums-1 slots, bucket sort

        for i in nums:
            count[i] = count.get(i, 0) + 1 #this gets the count of each number count[number] = count

        for s, c in count.items():#remember to use .items here
            freq[c].append(s) #freq[count] = number
         
        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        '''

        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] += 1
        
        for i, n in count.items():
            freq[n].append(i)
        
        rev = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                rev.append(j)
                if len(rev) == k:
                    return rev

        
        








        ''''
        count = {}
        freq = [[] for i in range(len(nums)+1)] # got error here, 

        for i in nums:
            count[i] = 1+ count.get(i, 0) # gonna add 1 here remember, don't need +=
        
        for k, v in count.items():
            freq[v].append(k)
        
        res= []
        for i in range(len(freq)-1, 0, -1): # remember it's len(freq) - 1, len(freq-1) will cause problems
            for j in freq[i]:
                res.append(j)
                if len(res) == k: # checking if the length fo the array that's created is of k length
                    return res

                    '''