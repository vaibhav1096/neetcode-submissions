class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setl=set()
        l=0
        resl=0
        for r in range(len(s)):
            while s[r] in setl:
                setl.remove(s[l])
                l+=1
            
            setl.add(s[r])
            resl=max(resl,r-l+1)
        return resl

        