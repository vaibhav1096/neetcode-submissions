class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1,1,2,8]
        [48,24,6,1]
        
        [1,-1,0,0,0]
        [0,6,6,3,1]

        prefix,postfix=[0 for i in range(len(nums))],[0 for i in range(len(nums))]
        pre=1
        for i in range(len(nums)):
            prefix[i]=pre
            pre=pre*nums[i]
        
        post=1
        for j in range(len(nums)-1,-1,-1):
            postfix[j]=post
            post=post*nums[j]
        
        res=[0 for i in range(len(nums))]
        for i in range(len(prefix)):
            res[i]=prefix[i]*postfix[i]
        return res



            
