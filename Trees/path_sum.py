# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
      if root is None:
            return False
        
      else:
        
        ans = False
        sum = targetSum - root.val
        if sum == 0 and root.right is None and root.left is None:
            ans = True
            
        ans = ans or self.hasPathSum(root.left,sum)
        ans = ans or self.hasPathSum(root.right,sum)
        
        return ans
        
        
        