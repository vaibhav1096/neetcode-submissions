class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        s1dictn={}
        for i in range(len(s1)):
            s1dictn[s1[i]]=1+s1dictn.get(s1[i],0)


        s2dictn={}
        l,r=0,0
        while r < len(s1):
            s2dictn[s2[r]]=1+s2dictn.get(s2[r],0)
            r+=1

        while r < len(s2):
            print(s1dictn,s2dictn,r)
            if s1dictn==s2dictn:
                return True
            else:
                s2dictn[s2[r]]=1+s2dictn.get(s2[r],0)
                s2dictn[s2[l]]-=1
                if s2dictn[s2[l]]==0:
                    s2dictn.pop(s2[l], None)
            l+=1
            r+=1
        return s1dictn == s2dictn

        