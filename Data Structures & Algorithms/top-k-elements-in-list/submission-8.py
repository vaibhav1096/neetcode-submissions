class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset=dict()
        for i in nums:
            hashset[i]=1+hashset.get(i,0)

        res = [[] for _ in range(len(nums)+1)] 
        print(res)
        for ke,v in hashset.items():
            res[v].append(ke)
        
        print(res)
        fres=[]    
        print(k)
        for i in range(len(nums),0,-1):
            for numi in res[i]:
                fres.append(numi)
                print(fres)
                if len(fres) == k:
                    return fres


            



            



        