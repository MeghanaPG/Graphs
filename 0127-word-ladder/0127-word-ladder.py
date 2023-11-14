class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Time Compolexity: O(n*m*m), BFS as we have to find the shortest path 
        if endWord not in wordList:
            return 0 

        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        # now build the adjacency list 
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        # the length is atleast going to be 1 
        res = 1 
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res 
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord) 
            res += 1 

        return 0 
            