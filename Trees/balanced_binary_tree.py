# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def height(self, root:TreeNode):
        
        if root is None:
            return 0
        
        l = self.height(root.left)
        r = self.height(root.right)
        
        return 1 + max(l,r)
        
    
    
    def isBalanced(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        return abs(self.height(root.left)- self.height(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        