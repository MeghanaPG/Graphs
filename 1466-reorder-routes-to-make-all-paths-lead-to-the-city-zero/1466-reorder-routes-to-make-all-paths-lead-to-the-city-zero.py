class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Time Complexity:
        # start at city 0 
        # recursively check its neighbours 
        # count outgoing edges 
        
        edges = {(a,b) for a, b in connections}
        neighbors = {city:[] for city in range(n)}
        # to keep track of visited nodes 
        visit = set()
        # count the number of edges we have to change 
        changes = 0 

        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        # traverse the graph
        def dfs(city):
            nonlocal edges, neighbors, visit, changes 

            for nei in neighbors[city]:
                if nei in visit:
                    continue 
                # check if this nei can reach city 0 
                if (nei, city) not in edges:
                    changes += 1 
                visit.add(nei)
                dfs(nei)
        visit.add(0)
        dfs(0)
        return changes
