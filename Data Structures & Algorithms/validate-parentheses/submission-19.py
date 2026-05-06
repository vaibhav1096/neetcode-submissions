class Solution:
    def isValid(self, s: str) -> bool:
        dictn={
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack=[]
        for i in s:
            if i in dictn.keys():
                if stack and stack[-1]==dictn[i]  :
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return False if stack else True
            
