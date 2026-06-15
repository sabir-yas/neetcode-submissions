# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:

        #order of conditions is necessary 
        if not t:
            return True
        if not s: # t is non empty if it get's here
            return False
        if self.sameTree(s,t): # return True if they are the same Tree
            return True
        
        #but what if they are not the sameTree, go left and right on s, check if 
        #either of them are true, then return true
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t or s.val != t.val:
            return False
            
        #if both nodes are not null and both are valid
        return (self.sameTree(s.left,t.left)
                and self.sameTree(s.right, t.right))
        
        



    