class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time Complexity: O(E+V)
        if not n:
            return True
        
        # create the adjacency list 
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            # the edges are undirected and hence we append each as their respective adj items 
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):
            # this will detect the cycle 
            if i in visit:
                return False 
            
            visit.add(i)
            # now we have to go through every single neighbour of i 
            for j in adj[i]:
                # this means if the prev node is already visited then we just continue
                if j == prev:
                    continue 
                # this means we have detected the cycle 
                if not dfs(j,i):
                    return False 
            return True 
        
        # here we are sending -1 as prev of 0 as it doesn't have any prev 
        # below the second condition makes sure that the graph is connected or it is a tree
        return dfs(0,-1) and n == len(visit)
