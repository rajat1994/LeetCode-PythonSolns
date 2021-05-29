# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def Symmetric (self, r:TreeNode, p:TreeNode)->bool:
        if r is None and p is None :
            return True
        
        if r is not None and p is not None :
            return r.val == p.val and (self.Symmetric(r.left,p.right)) and (self.Symmetric(r.right,p.left))
        
        else:
            return False
        
    def isSymmetric(self, root: TreeNode) -> bool:
        
        return self.Symmetric(root,root)