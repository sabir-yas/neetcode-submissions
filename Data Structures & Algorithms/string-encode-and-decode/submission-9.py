class Solution:

    def encode(self, strs: List[str]) -> str:
        #  5#Hello5#World

        res_str = ""
        for i in strs:
            res_str += str(len(i))+"#"+i
        
        return res_str

    def decode(self, s: str) -> List[str]:

        #5#Hello5#World want to go to Hello World
        i = 0
        res_arr = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
                len_str = int(s[i:j])

            res_arr.append(s[j+1:j+1+len_str])
            i = j + 1 + len_str

        return res_arr

