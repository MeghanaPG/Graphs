class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Graph, DFS 
        # Time Complexity: O(n+p)
        # for each crs we will have some prerequisites 
        if len(prerequisites) == 1:
            return True 

        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitset: all courses along dfs 
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False 
            if preMap[crs] == []:
                return True 
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False 
            visitSet.remove(crs)
            preMap[crs] = []
            return True 
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True 