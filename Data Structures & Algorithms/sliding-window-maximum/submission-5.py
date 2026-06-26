class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        l,r=0,0
        que=collections.deque() #indices
        while r < len(nums):

            # append to queue
            while que and nums[r] > nums[que[-1]]:
                que.pop()

            que.append(r)

            # check if left needs popping out
            if l > que[0]:
                que.popleft()

            # when to append
            if r+1 >= k:
                res.append(nums[que[0]])
                l+=1
            r+=1
        return res






        