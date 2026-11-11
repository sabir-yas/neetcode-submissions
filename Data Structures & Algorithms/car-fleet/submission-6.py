class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        paired = [(p,s) for p,s in zip(position, speed)]

        stack = []
        time = 0
        for p,s in sorted(paired)[::-1]:

            time = (target - p)/ s
            stack.append(time)

            if len(stack) >=2 and stack[-1] <= stack[-2]: #stack[-1] is the further one, so if the further car time is lesser than closer car time
                stack.pop()

        
        return len(stack)

