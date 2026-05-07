class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack1=[]
    
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack1 and temperatures[i] > stack1[-1][0]:
                val,ind=stack1.pop()
                res[ind]=i-ind

            stack1.append([temperatures[i],i])
        
        return res

            

        