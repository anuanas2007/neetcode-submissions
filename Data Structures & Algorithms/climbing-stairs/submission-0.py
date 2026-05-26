class Solution:
    def climbStairs(self, n: int) -> int:
        cur = dp2 = 0
        dp1 = 1

        for i in range(1,n+1):
            cur = dp1 + dp2
            cur, dp1, dp2 = 0, cur, dp1
        
        return dp1
        