# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.res = root.val

        def dfs(node):
            if not node:
                return 0
            leftMax  = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            self.res = max(self.res, node.val + leftMax + rightMax) #global update
            return node.val + max(leftMax, rightMax) #single best path

        dfs(root)
        return self.res