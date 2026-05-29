class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        ###brute force
        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                substr = s2[i : j + 1]
                substr = sorted(substr)
                if substr == s1:
                    return True
                
        return False
        '''
        if len(s1) > len(s2): # impossible to find s1 in s2 if s1 is longer
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] +=1
            s2Count[ord(s2[i]) - ord('a')] +=1
        
        matches =0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l =0 
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l+=1
        return matches == 26


































