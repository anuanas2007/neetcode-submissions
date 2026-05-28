class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            cur = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if cur + nums[l] + nums[r] == 0:
                    res.append([cur, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
                elif cur + nums[l] + nums[r] < 0: 
                    l += 1
                    
                else:
                    r -= 1
            
        return res

        