class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRoom(r,c):
            if (r <0 or c <0 or r == ROWS or c == COLS 
                or (r,c) in visit or rooms[r][c] == -1):
                return 
            visit.add((r,c))
            q.append([r,c])

        # adding the gates co-ordinates to q and visit set 
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        # BFS 
        dist = 0 
        while q:
            for i in range(len(q)):
                # first layer we are gonna be popping is the gates that we added 
                r,c = q.popleft()
                # we just have to modify the rooms array in place so we don't have to return anything 
                rooms[r][c] = dist 
                # this is for the neighbours 
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist += 1 
            # after we pop the gate, the next thing we are gonna be adding is all the layer which is 1 distance from the gate 
