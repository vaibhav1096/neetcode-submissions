class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="": 
            return ""
        
        l,r=0,0
        
        
        tdictn={}
        for i in range(len(t)):
            tdictn[t[i]]=1+tdictn.get(t[i],0)

        have,need=0,len(tdictn)
        
    
        sdictn={}
        res,resLen=[-1,-1],float("infinity")
        while r<len(s):
            c=s[r]
            sdictn[c]=1+sdictn.get(c,0)

            if c in tdictn and sdictn[c]==tdictn[c]:
                have+=1
            
            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                sdictn[s[l]]-=1
                if s[l] in tdictn and sdictn[s[l]]<tdictn[s[l]]:
                    have-=1
                l+=1

            r+=1
              
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
            
        






        