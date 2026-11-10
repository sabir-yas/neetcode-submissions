class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = []

        for i in tokens:
            
            if i in "+-/*":
                b = int(stack.pop())
                a = int(stack.pop())

                fin = 0

                if i == "+":
                    fin = a +b
                elif i == "-":
                    fin = a - b
                elif i == "*":
                    fin = a *b
                elif i == "/":
                    fin = int(a/b)
                stack.append(fin)
                    
            else:
                stack.append(int(i))
        
        return stack[0]