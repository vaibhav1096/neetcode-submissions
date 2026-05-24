# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res=[]
        if not root:
            return res
        que=collections.deque()
        que.append(root)
        while que:
            length=len(que)
            local=[]
            while length:
                node=que.popleft()
                local.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:    
                    que.append(node.right)
                length -= 1
            res.append(local[-1])
        return res
            
            
