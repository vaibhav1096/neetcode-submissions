class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        firs,lastr=0,len(matrix)-1
        row=-1
        while firs <=  lastr:
            mid=(firs+lastr)//2
            if target>=matrix[mid][0] and target<=matrix[mid][-1]:
                row=mid
                break
            elif target>=matrix[mid][-1]:
                firs=mid+1
            else:
                lastr=mid-1
        print(row)
        l,r=0,len(matrix[row])-1
        print(l,r)

        while l<=r:
            midel=(l+r)//2
            if matrix[row][midel]==target:
                return True
            elif matrix[row][midel]<target:
                l=midel+1
            else:
                r=midel-1

        return False


            



        
        

