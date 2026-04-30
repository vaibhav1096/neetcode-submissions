class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dictn=dict()

        # for i in range(len(numbers)):
        #     if numbers[i] in dictn:
        #         return [dictn[numbers[i]]+1,i+1]  
        #     else:
        #         dictn[target-numbers[i]]=i

        l,r=0,len(numbers)-1

        while l < r:
            if numbers[l]+numbers[r]>target:
                r-=1
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                return [l+1,r+1]

        
        