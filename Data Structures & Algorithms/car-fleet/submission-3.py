class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lis=[[p,s] for p,s in zip(position,speed)]
        print(lis)
        print(sorted(lis))
        stack=[]
        for pos,spe in sorted(lis)[::-1]:
            time = (target-pos)/spe
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)



        
        