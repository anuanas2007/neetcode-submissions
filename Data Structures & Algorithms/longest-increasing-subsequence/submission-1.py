class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS = [1] * len(nums)

        # for i in range(len(nums) - 1, -1, -1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] < nums[j]:
        #             LIS[i] = max(LIS[i], 1 + LIS[j])
        # return max(LIS)

        res = [nums[0]]

        def binsrch(arr, n):
            l = 0
            r = len(arr) - 1

            while l < r:
                mid = (l+r)//2
                if n > arr[mid]:
                    l = mid + 1
                if n <= arr[mid]:
                    r = mid
            
            return r
                

        for i in nums[1:]:
            if res[-1] < i:
                res.append(i)
            
            else:
                ind = binsrch(res, i)
                res[ind] = i
        
        return len(res)

        