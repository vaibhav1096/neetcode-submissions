class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix,postfix,res=[0]*len(nums),[0]*len(nums),[0]*len(nums)
        
        pre=1
        for i in range(len(nums)):
            prefix[i]=pre
            pre=pre*nums[i]
        
        post=1
        for j in range(len(nums)-1,-1,-1):
            postfix[j]=post
            post=post*nums[j]

        for i in range(len(prefix)):
            res[i]=prefix[i]*postfix[i]
        return res



            
