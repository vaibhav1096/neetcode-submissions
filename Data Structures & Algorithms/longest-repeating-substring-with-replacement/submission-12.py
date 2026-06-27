class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l=0
        res=0
        dictn={}
        for r in range(len(s)):
            dictn[s[r]]=1+dictn.get(s[r],0)

            if (r-l+1) - max(dictn.values()) > k:
                dictn[s[l]]-=1
                l+=1
            res=max(res,(r-l+1))
        
        return res

            
        