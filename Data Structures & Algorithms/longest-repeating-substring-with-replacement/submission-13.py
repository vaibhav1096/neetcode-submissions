class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictn={}
        l,r=0,0
        maxlen=0
        while r < len(s):
            dictn[s[r]]=1+dictn.get(s[r],0)
            if (r-l+1) - max(dictn.values()) > k:
                dictn[s[l]]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)    
            r+=1
        return maxlen
        