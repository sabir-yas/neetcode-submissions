from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap= defaultdict(list)

        for i in strs:
            count1 = [0] * 26
            for j in i:
                count1[ord(j)- ord("a")] += 1
            
            hashMap[tuple(count1)].append(i)
        
        return list(hashMap.values())
        