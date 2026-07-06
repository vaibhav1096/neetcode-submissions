class Solution:
    def isValid(self, s: str) -> bool:
        dictn={
            '}':'{',
            ']':'[',
            ')':'(',
        }
        stack=[]
        for string in s:
            if string in dictn.keys():
                if stack and stack[-1]==dictn[string]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(string)
        return True if not stack else False

        