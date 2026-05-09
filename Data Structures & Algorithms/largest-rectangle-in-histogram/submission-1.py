class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxArea=0

        for i in range(len(heights)):
            start=i
            while stack and stack[-1][1]>heights[i]:
                ind,val=stack.pop()
                maxArea=max(maxArea,val*(i-ind))
                start=ind

            stack.append([start,heights[i]])

        for i in stack:
            maxArea=max(maxArea,i[1]*(len(heights)-i[0]))
        
        return maxArea



        