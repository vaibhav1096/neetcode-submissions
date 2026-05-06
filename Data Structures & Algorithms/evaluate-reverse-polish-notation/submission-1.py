class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        


        def cal(a,b,char):
            if char=="+":
                return str(int(a)+int(b))
            elif char=="-":
                return str(int(a)-int(b))
            elif char=="*":
                return str(int(a)*int(b)) 
            elif char=="/":
                if int(b)==0:
                    return 0
                else:
                    return str(int(int(a)/int(b)))
        stack=[]
        for i in tokens:
            if i in ["+","-","*","/"]:
                b=stack.pop()
                a=stack.pop()
                stack.append(cal(a,b,i))
            else:
                stack.append(i)
        print(stack)
        return int(stack[0])
                  