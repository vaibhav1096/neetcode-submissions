class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        res=0
        charset=set()
        # charset.add(s[l])
        while r < len(s):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
           
            charset.add(s[r])
            res=max(res,r-l+1)
            print(charset,l,r)
            r+=1
        return res
            




             
         