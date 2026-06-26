class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        l,r=0,0
        maxr=0
        charset=set()
       
        while r < len(s):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            maxr=max(maxr, r-l+1)
            r+=1
        return maxr
        