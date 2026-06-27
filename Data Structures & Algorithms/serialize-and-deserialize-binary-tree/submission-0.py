# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #TODO: convert tree to string, preorder, root, left, right

        res=[]#["1", "2", "3"]

        def dfs(node):
            if not node:
                res.append("N") 
                return #want to break

            res.append(str(node.val)) # add the string val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #TODO: convert string back to tree
        vals = data.split(",")
        self.i=0

        def dfs():
            if vals[self.i]=="N":
                self.i+=1
                return None
            node = TreeNode(int(vals[self.i])) # creating node here, adding integer
            self.i+=1 #make sure to increase i
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
        
            
        
