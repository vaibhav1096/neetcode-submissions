class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        dictn={0:1}
        summ=0
        for n in nums:
            summ+=n
            diff=summ-k
            res = res + dictn.get(diff,0)
            dictn[summ] =  1 + dictn.get(summ,0)

        return res

        