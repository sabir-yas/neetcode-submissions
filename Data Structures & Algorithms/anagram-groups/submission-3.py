class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}
        # [1,0,1,0,0,1] : "act", "cat"
        
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord("a")]+=1

            hashMap[tuple(count)] = hashMap.get(tuple(count), []) + [i]
            
        return list(hashMap.values())
            



