class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # store key and values 
        # 2 conditions
        # town j must not be present in the key
        # town j must be present in the values 
        # Overall return the number which is not in keys and make sure it is present in values 
        # key -> [val1,val2,...]
        
        if len(trust) < n - 1:
            return -1

        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)

        for a,b in trust:
            outdegree[a] += 1 
            indegree[b] += 1

        
        for i in range(1, n+1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i 
            
        return -1