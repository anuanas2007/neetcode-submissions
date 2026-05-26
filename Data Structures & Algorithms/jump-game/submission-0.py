class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        farthest = nums[0]

        for i in range(len(nums)):
            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])
            if farthest >= target:
                return True
        