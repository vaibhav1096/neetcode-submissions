class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tempT={}
        window={}
        for i in t:
            tempT[i]=1+ tempT.get(i,0)
        
        have,need=0,len(tempT)
        res=[-1,-1]
        resL=float("inf")
        l=0

        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)

            if c in tempT and window[c]==tempT[c]:
                have+=1

            while have==need:
                if r-l+1 < resL:
                    res=[l,r]
                    resL=r-l+1
                window[s[l]] -= 1
                if s[l] in tempT and window[s[l]]<tempT[s[l]]:
                    have-=1
                l+=1

        l, r = res
        return s[l:r+1] if resL != float("inf") else ""  




        