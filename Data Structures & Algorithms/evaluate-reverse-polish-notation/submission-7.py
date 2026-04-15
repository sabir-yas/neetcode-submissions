class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        j = 0

        for i in tokens:
            if(i != "+" and i != "-" and i != "*" and i != "/"):
                stack.append(i)
            else:
                    b= int(stack.pop())
                    a = int(stack.pop())
                    if i == "+":
                        res = a + b
                    elif i == "-":
                        res = a - b
                    elif i == "*":
                        res = a * b
                    else:
                        res = a / b
                    stack.append(res)
                
        
        return int(stack[0])
                        
