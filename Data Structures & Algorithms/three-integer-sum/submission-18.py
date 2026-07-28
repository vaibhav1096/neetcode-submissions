class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums= sorted(nums)
        res=[]
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            
            l,r=i+1,len(nums)-1

            while l <r :
                add=nums[i]+nums[l]+nums[r]

                if add > 0:
                    r-=1
                elif add < 0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l+1]==nums[l]:
                        l+=1 
                    while l < r and nums[r-1]==nums[r]:
                        r-=1 
                    l+=1
                    r-=1
        return res


        

        
        