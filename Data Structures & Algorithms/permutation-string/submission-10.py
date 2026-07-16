class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1array=[0]*26
        s2array=[0]*26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1array[ord(s1[i])-ord("a")]+=1
            s2array[ord(s2[i])-ord("a")]+=1

        matches=0
        for c in range(26):
            if s1array[c]==s2array[c]:
                matches+=1
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True

            ind=ord(s2[r])-ord("a")
            s2array[ind]+=1
            if s2array[ind]==s1array[ind]:
                matches+=1
            elif s2array[ind]==s1array[ind]+1:
                matches-=1
                
            ind=ord(s2[l])-ord("a")
            s2array[ind]-=1
            if s2array[ind]==s1array[ind]:
                matches+=1
            elif s2array[ind]==s1array[ind]-1:
                matches-=1    

            l+=1
        return matches==26






        