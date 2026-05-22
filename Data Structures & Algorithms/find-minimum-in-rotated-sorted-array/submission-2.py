class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] <= nums[-1]:
            return nums[0]
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2

            if m > 0 and nums[m-1] > nums[m]:
                return nums[m]
            
            elif nums[l] <= nums[m] and nums[m] > nums[r]:
                l = m + 1
            
            else:
                r = m - 1
        return l       