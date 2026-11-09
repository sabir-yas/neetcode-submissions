class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        closeToOpen = {
            "}" : "{",
            "]" : "[",
            ")" : "(",
        }

        for i in s:
            
            #if closing bracket
            if i in closeToOpen and len(stack) !=0:
                opening = stack.pop()

                if closeToOpen[i] != opening:
                    return False

            #if opening bracket
            else:
                stack.append(i)

        return len(stack) == 0