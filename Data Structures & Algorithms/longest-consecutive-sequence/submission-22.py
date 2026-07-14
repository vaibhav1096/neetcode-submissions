class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        res=0
        for i in range(len(nums)):
            if nums[i]-1 not in numset:
                leng=1
                curr=nums[i]
                while curr+1 in numset:
                    leng+=1
                    curr+=1
                res=max(res,leng)
        return res



        