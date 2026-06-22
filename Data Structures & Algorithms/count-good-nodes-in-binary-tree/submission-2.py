# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(node, maxVal):  # Helper function that checks this node and its subtree, while carrying the max value seen so far

            if not node:  # If the current node is None, there are no good nodes here
                return 0  # Return 0 because an empty subtree contributes nothing
    
            res = 1 if node.val >= maxVal else 0  # Count this node if its value is at least the max value seen on the path
            maxVal = max(maxVal, node.val)  # Update the max value before passing it down to the children

            res += dfs(node.left, maxVal)  # Add the number of good nodes from the left subtree
            res += dfs(node.right, maxVal)  # Add the number of good nodes from the right subtree

            return res  # Return the total number of good nodes in this subtree


        return dfs(root, root.val)  # Start DFS at the root, with the root value as the first max value

        



    
