class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r=0,len(nums)-1
        res=99999999999999
        while l<=r:
            mid = (l+r)//2
            res=min(res,nums[mid])
            if nums[mid]>nums[l] : 
                if   l<=r and nums[l] > nums[r] :
                    l=mid+1
                else:
                    r=mid-1
            else:
                if  l<=r and nums[mid]<nums[l] :
                    r=mid-1
                else:
                    l=mid+1
        return res
        

        