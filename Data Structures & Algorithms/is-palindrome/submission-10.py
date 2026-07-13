class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isvalid(n):
            return ord("a")<=ord(n)<=ord("z") or ord("A")<=ord(n)<=ord("Z") or ord("0")<=ord(n)<=ord("9")
        l,r=0,len(s)-1

        while l < r:
            while  l < r and  not  isvalid(s[l]):
                l+=1

            while  l < r and  not  isvalid(s[r]):
                r-=1

            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True