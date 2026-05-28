class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for r in range(m):
            for c in range(n//2):
                matrix[r][c], matrix[r][n-c-1] = matrix[r][n-c-1], matrix[r][c]
        
        