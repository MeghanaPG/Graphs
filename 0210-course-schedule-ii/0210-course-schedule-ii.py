class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        resSet = set()
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        # a crs has 3 possible states 

        # visited -> crs has been added to the output 

        # visiting -> crs not added to output, but added to cycle 

        # unvisited -> crs not added to output or cycle 
        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True 

            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False 
            # because it's no longer in the path we are going 
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True 

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
            