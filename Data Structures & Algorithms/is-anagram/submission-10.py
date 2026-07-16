class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictn1={}
        dictn2={}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            dictn1[s[i]]=1+dictn1.get(s[i],0)
            dictn2[t[i]]=1+dictn2.get(t[i],0)
        
        return dictn1==dictn2


        