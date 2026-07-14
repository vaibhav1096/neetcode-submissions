class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictn={}
        for i in range(len(nums)):
            if nums[i] not in dictn:
                dictn[target-nums[i]]=i
            else:
                return [dictn[nums[i]],i]
        