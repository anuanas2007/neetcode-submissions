class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur = 0

        for i in nums:
            if cur + i < i:
                cur = i
            else:
                cur += i
            
            res = max(cur, res)

        return res