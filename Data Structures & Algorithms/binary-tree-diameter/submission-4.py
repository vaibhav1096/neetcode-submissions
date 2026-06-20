# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdia=0

        def dfs(root):
            nonlocal maxdia
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            maxdia=max(maxdia, dfs(root.left)+dfs(root.right))
            return 1+max(dfs(root.left),dfs(root.right))
        dfs(root)
        return maxdia