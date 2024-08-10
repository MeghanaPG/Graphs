class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time Complexity: O(n+p)
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(crs):
            # indicates a loop
            if crs in visit:
                return False 
            # no pre 
            if preMap[crs] == []:
                return True 
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False 
            visit.remove(crs)
            # bcz it will be true 
            preMap[crs] = []
            return True

        # manually check each course as they may not be connected  
        for crs in range(numCourses):
            if not dfs(crs):
                return False 
        return True 