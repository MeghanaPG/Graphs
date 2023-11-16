class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Time Complexity: O(V+E)
        par = [i for i in range(n)]
        rank = [1] * n

        # this function is to find the parent 
        def find(n1):
            res = n1
            # while res is != parent of itself 
            while res !=par[res]:
                # we will link the parent of res to its grand parent 
                par[res] = par[par[res]]
                res = par[res]
            return res 

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2] 
            # this indicates that we performed a successful union 
            return 1 
        
        res = n 
        for n1,n2 in edges:
            # every time we perform an union the number of connected components will decrease 
            res -= union(n1,n2)
        return res
