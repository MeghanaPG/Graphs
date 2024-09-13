class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        output = []
        visit = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False 
            if crs in visit:
                return True
            cycle.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False 
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True 
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
        



                

            
            
            