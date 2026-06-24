# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #the order we popped the stack-> get the kth
        #inorder traversal- left, root, right,
        #use a stack so we can keep going left, then we start popping left , we can go back to root, pop it then go to right
        #iterative dfs style

        n= 0 # so that we get kth smallest
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n+=1
            if n == k:
                return cur.val
            cur = cur.right
        
        return 
