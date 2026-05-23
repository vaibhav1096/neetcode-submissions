# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        
        if not subRoot and not root:
            return True
        
        return self.isSubtree(root.left,subRoot) or  self.isSubtree(root.right,subRoot) or self.same(root,subRoot)
    
    def same(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        if self.same(root1.left,root2.left) and self.same(root1.right,root2.right) and root1.val==root2.val :
            return True
        else:
            return False


        