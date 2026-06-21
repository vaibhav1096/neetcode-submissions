# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que=collections.deque()

        res=[]
        que.append(root)
        while que:
            length=len(que)
            for i in range(length):
                currnode=que.popleft()
                if i == length - 1:
                    res.append(currnode.val)
                if currnode.left:
                    que.append(currnode.left)
                if currnode.right:
                    que.append(currnode.right)
            # res.append(currnode.val)

        return res
        