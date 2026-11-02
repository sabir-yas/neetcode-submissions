class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        revMap = [0] * 26
        for i in s:
            revMap[ord(i) - ord("a")]+=1
        
        for j in t:
            revMap[ord(j) - ord("a")]-=1
        
        return revMap == [0] * 26
    

    '''
    if (s.length() != t.length()){
        return false
    }

    unordered_map<char, int> countS;
    unordered_map<char, int> countT;
    for (int i=0; i< s.length(); i++){
        countS[s[i]]++;
        countT[t[i]]++;
    }
    return countS == countT;

    '''