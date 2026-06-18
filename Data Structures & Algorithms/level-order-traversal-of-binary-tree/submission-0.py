# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        q= collections.deque([root]) #root
        
        arr=[]
        while q:
            level=[]
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                arr.append(level)
    

        return arr    
    
        '''
        if node.left: #can't do this, becuz 1st time we want to add the 1st node
                    level.append(node.left.val)
                if node.right:
                    level.append(node.right.val)
        '''
            
        