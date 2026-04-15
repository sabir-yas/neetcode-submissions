class Solution:
    def isValid(self, s: str) -> bool:
        
        
        bracks = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
        '''
        stack = []

        for i in s:
            if i == "{" or i == "(" or i == "[":
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == bracks[stack[-1]]:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0 
        '''
        #neet's version
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

