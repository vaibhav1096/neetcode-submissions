class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r=1,max(piles)
        res=r

        while l <= r:
            mid = (l+r)//2
            time=0

            for p in piles:
                val=p
                time += (p + mid - 1) // mid
                # while val:
                #     time = time + 1
                #     val=val%mid
            
            if time <= h:
                
                res=mid
                r=mid-1
            else: 
                l=mid+1
        return res

                
                

            



        