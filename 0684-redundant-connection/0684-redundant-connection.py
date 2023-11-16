class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges) + 1)

        # we will first write the find part of Unionfind algorithm 
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p 
        
        # in the union part, we have to find it's root parent 
        #  return false if they have the same parent, because with that we cannot complete union operation 
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False 
            
            if rank[p1] > rank[p2]:
                # p1 is gonna be the parent of p2 
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True 
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
