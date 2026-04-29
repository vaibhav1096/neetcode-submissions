class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # nums=set(nums)
        # maxlen=1
        # for i in nums:
        #     streak=1
        #     while i-1 in nums:
        #         streak+=1
        #         i=i-1
        #     maxlen=max(maxlen,streak)
        # return maxlen

        nums=sorted(nums)
        maxstreak,streak=1,1
        for i in range(1,len(nums)):
            if abs(nums[i]-nums[i-1])==1:
                streak+=1
            elif nums[i]==nums[i-1]:
                i+=1
            else:
                streak=1
            maxstreak=max(maxstreak,streak)
        return maxstreak




        