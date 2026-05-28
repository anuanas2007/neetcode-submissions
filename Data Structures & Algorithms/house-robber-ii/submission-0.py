class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(hs):
            if len(nums) <= 2:
                return max(nums)

            dp1 = hs[0]
            dp2 = max(dp1, hs[1])

            for i in range(2, len(hs)):
                temp = max(hs[i] + dp1, dp2)
                dp1, dp2 = dp2, temp
            
            return dp2
        

        return max(helper(nums[:len(nums)-1]), helper(nums[1:]))
                
                

        
        