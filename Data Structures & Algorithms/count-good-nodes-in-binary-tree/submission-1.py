# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curmax=root.val
        self.res=0
        def dfs(node,curmax):
            if not node:
                return
            if node.val >= curmax:
                self.res+=1
                curmax=max(curmax,node.val)
            dfs(node.right,curmax)
            dfs(node.left,curmax)
        dfs(root,curmax)
        return self.res



        