class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictn=collections.defaultdict()
        l=0
        maxlen=0
        for r in range(len(s)):
            dictn[s[r]]=1+ dictn.get(s[r],0)
            if (r-l+1) - max(dictn.values()) > k:
                dictn[s[l]]-=1
                l+=1
            
            maxlen=max(maxlen,r-l+1)

        return maxlen


        