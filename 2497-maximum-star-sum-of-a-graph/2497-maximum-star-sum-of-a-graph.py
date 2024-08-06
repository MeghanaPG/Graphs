class Solution:
    def maxStarSum(self, vals, edges, k):
        N = len(vals)
        e = collections.defaultdict(list)

        # Build the adjacency list with positive neighbor values
        for u, v in edges:
            if vals[v] > 0:
                e[u].append(vals[v])
            if vals[u] > 0:
                e[v].append(vals[u])

        # Sort neighbors' values in descending order for each node
        for v in e.keys():
            e[v].sort(reverse=True)

        best = float('-inf')  # Initialize with a very low number

        # Calculate the maximum star sum
        for i in range(N):
            star_sum = vals[i] + sum(e[i][:k])
            best = max(best, star_sum)

        return best