class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        dirs = [(-1,0), (0,-1), (1,0), (0,1)]

        a = []
        p = []

        for i in range(n):
            p.append((0,i))
            a.append((m-1,i))
        
        for j in range(m):
            p.append((j, 0))
            a.append((j, n-1))
        
        def bfs(arr, oc):
            q = deque(arr)
            while q:
                r, c = q.popleft()
                oc[r][c] = True

                for dir in dirs:
                    nr, nc = dir[0]+r, dir[1]+c
                    if 0<=nr<m and 0<=nc<n and not oc[nr][nc] and heights[nr][nc]>=heights[r][c]:
                        q.append((nr, nc))

        
        bfs(a,atl)
        bfs(p,pac)
        
        res = []
        for r in range(m):
            for c in range(n):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        
        return res

        