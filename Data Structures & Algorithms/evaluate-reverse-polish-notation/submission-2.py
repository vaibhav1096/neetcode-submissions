class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if char=="+":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(str(a+b))
            elif char=="-":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(str(b-a))
            elif char=="*":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(str(b*a)) 
            elif char=="/":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(str(int(b/a)))
            else:
                stack.append(char)
        return int(stack[0])
