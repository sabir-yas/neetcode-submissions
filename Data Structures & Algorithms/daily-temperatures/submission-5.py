class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        arr= [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            #if cur temp is greater than temp we started with
            while stack and t > stack[-1][1]:
                stackInd, stackTmp = stack.pop()   
                arr[stackInd] = i - stackInd

            #else add
            stack.append((i,t))
        
        return arr