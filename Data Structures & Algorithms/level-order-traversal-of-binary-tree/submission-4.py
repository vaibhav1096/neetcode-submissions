# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que=collections.deque()
        que.append(root)
        res=[]
        while que:
            lis=[]
            length=len(que)
            for i in range(length):
                curnode=que.popleft()
                lis.append(curnode.val)
                if curnode.left:
                    que.append(curnode.left)
                if curnode.right:
                    que.append(curnode.right)
            res.append(lis)
        return res




        