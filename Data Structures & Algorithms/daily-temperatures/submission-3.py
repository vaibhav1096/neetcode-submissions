class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*(len(temperatures))
        for i in range(len(temperatures)):
            print(stack)
            while stack and stack[-1][1]<temperatures[i]:
                ind,val=stack.pop()
                res[ind]=i-ind
           
            stack.append((i,temperatures[i]))
        return res


        