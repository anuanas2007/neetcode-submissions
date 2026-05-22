class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        res = 0

        def dfs(row, col):
            grid[row][col] = "0"
            stack = deque()
            stack.append([row,col])
            while stack:
                r,c = stack.popleft()
                for dir in dirs:
                    nr, nc = dir
                    if 0<=r+nr<m and 0<=c+nc<n and grid[r+nr][c+nc] == "1":
                        stack.append([r+nr, c+nc])
                        grid[r+nr][c+nc] = "0"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
        
        return res
        