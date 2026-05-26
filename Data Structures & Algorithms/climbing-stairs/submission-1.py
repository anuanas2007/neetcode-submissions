class Solution:
    def climbStairs(self, n: int) -> int:
        dp2 = 0
        dp1 = 1

        for i in range(1,n+1):
            temp = dp1 + dp2
            dp1, dp2 = temp, dp1
        
        return dp1
        