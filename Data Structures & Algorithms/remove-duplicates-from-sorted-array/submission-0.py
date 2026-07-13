class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # hashset=set()
        ind=1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[ind]=nums[r]
                ind+=1
        return ind


        