class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset=set(nums)
        
        maxl=float("-inf")
        for num in nums:
            localLen=1
            i=num
            while i-1 in hashset:
                localLen+=1
                i-=1
            maxl=max(maxl,localLen)
        return maxl

            
            

        