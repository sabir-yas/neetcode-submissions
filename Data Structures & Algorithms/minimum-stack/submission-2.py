class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        #val = min(val, self.minstack[-1] if self.minstack else val)
        #self.minstack.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])
        self.minstack.append(val)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop() #gotta pop minstack too

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        

    '''
    def push(self, val):
        stack.append(val)
        if minstack and val < minstack[-1]:
            minstack.append(val)
    '''

























