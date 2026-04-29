class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=set(nums)
        maxlen=1
        for i in nums:
            streak=1
            while i-1 in nums:
                streak+=1
                i=i-1
            maxlen=max(maxlen,streak)
        return maxlen



        