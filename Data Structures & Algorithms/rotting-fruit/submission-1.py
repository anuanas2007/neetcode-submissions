class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        rotten = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append([i,j])
        
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        q = deque(rotten)
        time = 0

        while q and fresh > 0:
            time += 1
            for a in range(len(q)):
                r, c = q.popleft()
                for di in dirs:
                    nr, nc = r+di[0], c+di[1]
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append([nr, nc])
        
        if fresh == 0:
            return time
        else:
            return -1
        