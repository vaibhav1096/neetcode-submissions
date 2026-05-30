class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap= {i:[] for i in range(numCourses)}

        for i in prerequisites:
            preMap[i[0]].append(i[1])
        
        visit=set()

        def dfs(node):
            if preMap[node]==[]:
                return True
            
            if node in visit:
                return False

            visit.add(node)
            for i in preMap[node]:
                if not dfs(i):
                    return False
            visit.remove(node)
            preMap[node] = []
            return True

        for c in preMap.keys():
            if not dfs(c):
                return False
        return True
            

        