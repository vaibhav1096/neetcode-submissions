class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictn=dict()

        for i in range(len(numbers)):
            if numbers[i] in dictn:
                return [dictn[numbers[i]]+1,i+1]  
            else:
                dictn[target-numbers[i]]=i
        
        