# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #brute force- (On square)


        #my approach- didn't take into account the global comparision checks. like it checked a subtree but didn't compare with the topmost root.
        '''
        start with -inf, +inf
        go down left subtree- check left < root-> -inf < 3 < 5 
        go down right subtree- check right > root-> 5 <7 < inf
        4 < 7-> borrow from parent. 5 < 4< 7- false
        '''
        
        def valid(node, left, right): # left and right are the allowed value boundaries for the current node
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right,node.val,right)

        return valid(root, float("-inf"), float("inf")) #no restriction on what the root value can be