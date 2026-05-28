class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        tree = TrieNode()
        def add(word):
            cur = tree
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.end = True
        
        for w in words:
            add(w)
    
        m = len(board)
        n = len(board[0])
        res = set()
        path = set()

        def dfs(r, c, cur, wor):
            if r<0 or c<0 or r>=m or c>=n or (r,c) in path or board[r][c] not in cur.children:
                return

            path.add((r,c))
            cur = cur.children[board[r][c]]
            wor += board[r][c]
            if cur.end:
                res.add(wor)

            dfs(r + 1, c, cur, wor)
            dfs(r - 1, c, cur, wor)
            dfs(r, c + 1, cur, wor)
            dfs(r, c - 1, cur, wor)  

            path.remove((r,c))       

        for i in range(m):
            for j in range(n):
                dfs(i,j, tree, "")
        
        return list(res)

        