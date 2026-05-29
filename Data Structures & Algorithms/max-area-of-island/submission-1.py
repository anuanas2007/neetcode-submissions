class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        res = 0

        def bfs(r,c):
            cur = 0
            q = deque()
            q.append((r,c))
            grid[r][c] = 0

            while q:
                ro, co = q.popleft()
                cur += 1

                for dir in dirs:
                    nr, nc = ro + dir[0], co + dir[1]
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return cur
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    re = bfs(i,j)
                    res = max(res, re)
        
        return res




        