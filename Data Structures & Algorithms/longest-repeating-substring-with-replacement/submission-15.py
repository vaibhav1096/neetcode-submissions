class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictn={}
        res=0
        l,r=0,0

        for r in range(len(s)):
            dictn[s[r]]=1+dictn.get(s[r],0)
            if l < r and (r-l+1)-max(dictn.values()) > k:
                dictn[s[l]]-=1
                l+=1
            res = max(r-l+1,res)

        return res

        