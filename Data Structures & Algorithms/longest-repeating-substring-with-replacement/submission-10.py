class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset={}
        l,r=0,0
        maxl=0
        while r < len(s):
            charset[s[r]]=1+charset.get(s[r],0)

            if (r-l+1)-max(charset.values())>k:
                charset[s[l]]-=1
                l+=1
            maxl=max(maxl,(r-l+1))
            r+=1

        return maxl

        
        