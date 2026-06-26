class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        l,r=0,0
        que=collections.deque() #indices
        while r < len(nums):

            while que and nums[r] > nums[que[-1]]:
                que.pop()

            que.append(r)

            if l > que[0]:
                que.popleft()

            if r+1 >= k:
                res.append(nums[que[0]])
                l+=1
            r+=1
        return res






        