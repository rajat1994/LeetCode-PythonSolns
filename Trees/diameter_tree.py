# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__ (self):
        self.res = 0
        
        
    def diameter (self, root):
        
        if root is None:
            return 0
        
        l = self.diameter(root.left)
        r = self.diameter(root.right)
        
        temp = 1 + max(l,r)
        ans = max(temp, 1+l+r)
        self.res = max(self.res, ans)
        
        return temp
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.diameter(root)
        return self.res - 1
    
    