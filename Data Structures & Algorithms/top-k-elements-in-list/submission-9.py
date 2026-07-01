class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countT={}
        for n in nums:
            countT[n]=1+countT.get(n,0)
        
        midRes = [[] for _ in range(len(nums) + 1)]
        for ind,val in countT.items():
            midRes[val].append(ind)
        
        res=[]
        for r in  range(len(midRes)-1,0,-1):
            for c in midRes[r] :
                res.append(c)
                if len(res)==k:
                    return res

            




        