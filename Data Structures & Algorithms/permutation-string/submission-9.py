class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lis1,lis2 = [0]*26, [0]*26
        matches=0
        l=0

        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            lis1[ord(s1[i])-ord('a')]+=1
            lis2[ord(s2[i])-ord('a')]+=1
        
        for c in range(26):
            if lis1[c]==lis2[c]:
                matches+=1
        
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True

            index=ord(s2[r])-ord('a')
            lis2[index]+=1
            if lis2[index]==lis1[index]:
                matches+=1
            elif lis2[index]==lis1[index]+1:
                matches-=1

            index=ord(s2[l])-ord('a')
            lis2[index]-=1
            if lis2[index]==lis1[index]:
                matches+=1
            elif lis2[index]==lis1[index]-1:
                matches-=1
            l+=1
        return matches==26
            





