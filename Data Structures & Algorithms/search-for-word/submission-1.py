class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        path = set()

        def dfs(r, c, le):
            if le == len(word):
                return True

            path.add((r,c))
            for dir in dirs:
                nr, nc = r+dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == word[le] and (nr,nc) not in path:
                    if dfs(nr, nc, le + 1):
                        return True
            path.remove((r,c))
        
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j, 1):
                        return True
        
        return False
        