class Solution:
    def numDecodings(self, s: str) -> int:
        cur = dp2 = 0
        dp1 = 1

        for i in range(len(s) -1, -1, -1):
            if s[i] == "0":
                cur = 0

            else:
                cur = dp1

            if i < len(s) - 1 and (s[i] == "1" or s[i] =="2" and s[i+1] in "0123456"):
                cur += dp2

            cur, dp1, dp2 = 0, cur, dp1

        return dp1 