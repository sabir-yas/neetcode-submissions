class Solution:
    def isValid(self, s: str) -> bool:
        bracks = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

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

